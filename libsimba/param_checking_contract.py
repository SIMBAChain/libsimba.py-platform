from typing import List, Optional, Any, Dict
from libsimba.decorators import auth_required
from libsimba.utils import build_url
import requests


class ParamCheckingContract:
    def __init__(self, base_api_url, app_name, contract_name):
        self.app_name = app_name
        self.contract_name = contract_name
        self.base_api_url = base_api_url
        self.contract_uri = "{}/contract/{}".format(self.app_name, self.contract_name)
        self.async_contract_uri = "{}/async/contract/{}".format(self.app_name, self.contract_name)
        self.metadata = self.get_metatadata()
        self.params_restricted = self.param_restrictions()

    @auth_required 
    def get_metadata(self, headers):
        url = build_url(self.base_api_url, "v2/apps/{}/contract/{}/?format=json".format(self.app_name, self.contract_name)) 
        return requests.get(url, headers=headers)

    def is_array(self, param) -> bool:
        return param.endswith(']')

    def array_restrictions(self, arr:str) -> dict:
        """
        returns a dictionary that maps dimension to array-length restriction
        Our outer-most array is associated with our lowest dimension: 0

        for example, 'uint256[5][3][][4]' would get mapped to: {0: '5', 1: '3', 2: None, 3: '4'}

        Args:
            arr (str): string formatted solidity style array, eg 'uint256[5][3][][4]'

        Returns:
            [dict]: dict mapping of dimension -> array-length, eg {0: '5', 1: '3', 2: None, 3: '4'}
        """
        arr_lengths = {}
        for i in range(self.get_dimensions(arr)):
            arr_len = arr[arr.find('[')+1:arr.find(']')]
            arr_lengths[i] = int(arr_len) if arr_len else None 
            arr = arr[arr.find(']')+1:]
        return arr_lengths

    def get_dimensions(self, param:str, dims:Optional[int] = 0) -> int:
        """
        Recursive function to determine dimensions of array type

        Args:
            param (str): string formatted parameter (eg 'str[][]' will return 2)
            dims (Optional[int], optional): [description]. Defaults to 0.

        Returns:
            [int]: number of dimensions in array
        """
        if '[' not in param:
            return dims 
        param = param[param.find('[')+1:]
        dims += 1 
        return self.get_dimensions(param, dims)
    
    def param_restrictions(self) -> dict:
        """
        This will return a dictionary of methods that have either array parameters with length restrictions,
        or uint parameters. This includes methods that have dynamic (non-length restricted) parameters for 
        which the elements are uints.

        If a method does NOT have one of the following:
            fixed-length (length-restricted) array parameters
            uint parameters
            fixed-length or dynamic array parameters whose elements are uints or uint-elemented arrays

            then the method WILL NOT be included in our return array. 
            This will allow for a quick check when we call each method to ask whether we need to check 
            param restrictions
        
        Note that if a method does not have any params with array length restrictions, then the key 
        'array_params' will not be populated for that method in our return object
        Similarly, if a method does not have any params that are uints, then the key 'uint_params'
        will not be populated for that method in our return object

        Returns:
            [dict]: 
            example return for a contract with methods 'an_arr', 'array_params', and 'bbb':

            {'an_arr': {'array_params': {'first': {0: None, 'contains_uint': True}}},
            'another_uint_param': {'uint_params': ['another_uint', 'second_uint']},
            'bbb': {'array_params': {'first': {0: None, 1: None, 'contains_uint': True}}}
            }
        """
        md = self.metadata
        contract = md['contract']
        paramRestrictions = {}
        methods = {method: values for method, values in contract['methods'].items()}
        for method, params in methods.items():
            for paramDict in params['params']:
                paramName = paramDict['name']
                rawType = paramDict['type']
                contains_or_is_uint = rawType.startswith('uint')
                # don't do anything if not an array and not contains_or_is_uint
                # we're only worried about uint type checking and array length checking
                if not contains_or_is_uint and not self.is_array(paramName):
                    continue
                if method not in paramRestrictions:
                    paramRestrictions[method] = {}
                if contains_or_is_uint and not self.is_array(rawType):
                    # we are just keeping a list of paramNames for params that are uint_params
                    if 'uint_params' not in paramRestrictions[method]:
                        paramRestrictions[method]['uint_params'] = [paramName]
                    else:
                        paramRestrictions[method]['uint_params'].append(paramName)
                elif self.is_array(rawType):
                    if 'array_params' not in paramRestrictions[method]:
                        paramRestrictions[method]['array_params'] = {}
                    arrRestrictions = self.array_restrictions(rawType)
                    arrRestrictions['contains_uint'] = contains_or_is_uint
                    paramRestrictions[method]['array_params'][paramName] = arrRestrictions
        return paramRestrictions

    def check_array_restrictions(self, arr:List[Any], param_name, param_restrictions_dict:dict, level=0):
        """
        recursively checks lengths of arrays and sub-arrays for parameter
        if element of an array is not an array, and there are uint restrictions for the parameter,
        then we check to make sure that the element is an int >= 0

        we also compare elements in each array to make sure there is no element mixing

        Args:
            arr (List[Any]): list to have lengths and elements checked
            param_name ([type]): parameter name - required to look up array dimension requirements
            param_restrictions_dict (Dict): restriction dict derived from a particular method's key in self.param_restrictions() call
                eg  {'first': {0: None, 'contains_uint': True}}
            level (int, optional): recursively increases for increasing dimensions. Defaults to 0.

        Raises:
            ValueError: [description]
            TypeError: [description]
            TypeError: [description]
            ValueError: [description]

        Returns:
            [bool]: True if no exceptions raised
        """
        level_restriction = param_restrictions_dict[param_name][level]
        if level_restriction is not None:
            if len(arr) != level_restriction:
                raise ValueError("array length error")
        level += 1
        for i, element in enumerate(arr):
            # first check to make sure that if one element is list, all elements are lists
            if i > 0 and type(arr[i]) != type(arr[i-1]):
                raise TypeError("array element types do not match")
            # then recursively check each sublist
            if type(element) == list:
                self.check_array_restrictions(element, param_name, param_restrictions_dict, level=level)
            else:
                if param_restrictions_dict[param_name]['contains_uint'] is True:
                    if type(element) != int:
                        raise TypeError("final sub array elements must be type int") 
                    if element < 0:
                        raise ValueError("final sub array elements must be non-negative")
        return True

    def check_uint_restriction(self, param_value:int):
        """
        check that parameter value is int >= 0

        Args:
            param_value (int): [description]

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            [bool]: True if no exceptions are raised
        """
        if param_value < 0:
            raise ValueError("parameter value must be >= 0")
        if type(param_value) != int:
            raise ValueError("parameter must be type int")
        return True

    def validate_params(self, method_name:str, inputs:dict):
        """
        should be called at any method call that requires inputs
        calls check_uint_restrictions and check_array_restrictions

        Args:
            method_name (str): method name for which we are checking validating parameters
            inputs (dict): dict of inputs of {'param_name_string': param_value} form

        Returns:
            [bool]: True if no exceptions are raised
        """
        paramRestrictions = self.params_restricted
        method_restrictions = paramRestrictions.get(method_name, None)
        if not method_restrictions:
            # this means the method had no array length or uint restrictions
            return True
        uint_params = paramRestrictions.get('uint_params', {})
        array_params = paramRestrictions.get('array_params', {})
        for param_name, param_value in inputs.items():
            if param_name in uint_params:
                self.check_uint_restriction(param_value)
            if param_name in array_params:
                self.check_array_restrictions(param_value, param_name, array_params)
        return True