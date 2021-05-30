from typing import List, Tuple, Dict, Optional, Union, Any
import json 
from jinja2 import Environment, FileSystemLoader 
import requests
from libsimba.decorators import auth_required
from libsimba.utils import build_url

class SimbaHintedContract:
    def __init__(
        self, 
        metaData: str, 
        appName: str, 
        baseAPIurl: str = 'https://api.sep.dev.simbachain.com/',
        contractTemplate: str ='contract.tpl', 
        outputFile: str = 'newContract.py',
        templateFolder: str ='templates',
        contractName: str = None # we will need to pass this once outside of testing
        ):
        """
        SimbaHintedContract allows us to represent our smart contract as a Python class
        The purpose of this class is largely to provide an SDK that utilizes type hinting 
        and exposes method calls instead of python get requests
        Note that the underlying functionality is still contained in https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py

        Args:
            metaData (str): string formatted json metadata from our smart contract
            appName (str): name of the app that accesses our smart contract
            baseAPIurl (str, optional): Defaults to 'https://api.sep.dev.simbachain.com/'.
            contractTemplate (str, optional): name of the jinja template used to create .py version of contract code. Defaults to 'contract.tpl'.
            outputFile (str, optional): name of .py file we wish to write our .py version of contract to. Defaults to 'newContract.py'.
            templateFolder (str, optional): folder contianing our jinja template. Defaults to 'templates'.
        """
        # will need to rewrite logic to access metadata
        # self.contract_name = contractName # will uncomment this after testing
        self.app_name = appName
        self.metadata = json.load(open(metaData, 'r'))
        # self.metadata = self.get_metadata() # this line will be uncommented after testing
        self.contract = self.metadata['contract']
        self.contract_name = self.contract['name'] # remove after testing
        self.contract_methods = self.contract['methods']

        self.base_api_url = baseAPIurl
        self.contract_template = contractTemplate 
        self.output_file = outputFile
        self.template_folder = templateFolder
        self.struct_names = {fullName: fullName.split('.')[1] for fullName in self.contract['types']}

    @auth_required 
    def get_metadata(self, headers):
        url = build_url(self.base_api_url, "v2/apps/{}/contract/{}/?format=json".format(self.app_name, self.contract_name)) 
        return requests.get(url, headers=headers)
    
    def accepts_files(self, method_name:str) -> bool:
        """
        returns a bool indicating whether method_name accepts files or not, as indicated by whether
        _bundleHash is present as a parameter name in method_name's parameters

        Args:
            method_name (str): method_name for which we want to determine if files are accepted or not

        Returns:
            bool: 
        """
        for param in self.contract_methods[method_name]['params']:
            if param['name'] == '_bundleHash':
                return True 
        return False
    
    def file_methods(self) -> List[str]:
        """
        returns a list of method names that accept files. 
        
        Not currently used.

        Returns:
            List[str]: list of contract methods that accept files
        """
        return [method for method in self.contract_methods if self.accepts_files(method)]

    def return_data_types(self, method_name:str, as_dict=False) -> Union[List, Dict]:
        """
        get the native Python data types for return values from contract methods

        Args:
            method_name (str): method_name to obtain return data type for
            as_dict (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        m = self.contract_methods.get(method_name, None)
        if as_dict:
            result = {}
        else:
            result = []
        if not m:
            return None
        for i, r in enumerate(m.get('returns', [])):
            dt = r['type'] # come back and handle type later
            nativeType = self.native_python_type(r)
            if as_dict:
                result[str(i)] = nativeType
            else:
                result.append(nativeType)
        return result

    def handle_array(self, fullType:str, basicType:str) -> str:
        """
        handle_array is meant to handle arrays and nested arrays, and return a string formatted version of that nested array

        Args:
            param (app_metadata.DataType): method parameter, of type DataType, for which we want to obtain a native Python data type hint
            paramType (str): native Python type obtained in native_python_type (int, str, etc.)

        Returns:
            arrType (str): string formatted version of array or nested array
        """
        arrType = f'List[{basicType}]'
        for _ in range(self.get_dimensions(fullType)-1):
            arrType = f'List[{arrType}]'
        return arrType

    def is_array(self, param):
        return param.endswith(']')

    def handle_struct(self, structParam: str, forward_reference:bool = False):
        """
        gives us custom struct type, accounting for array

        Args:
            structParam (str): struct in either Contract.Struct or Contract.Struct[]...[] format

        Returns:
            [str]: string in either 'libsimba.Contract.Struct' or 'List[libsimba.Contract.Struct]'form
        """
        if self.is_array(structParam):
            structType = structParam[:structParam.find('[')]
            # should 'libsimba' below be local directory instead?
            if forward_reference:
                structType = f'"{structType}"'
            return structType
        if forward_reference:
            structType = f'"{structParam}"'
        else:
            structType = structParam
        return structType

    def convert_classes_to_dicts_nested(self):
        """
        function for producing a class that has methods for converting a class instance to a dict
        this function would be used in our .tpl doc if we wanted to declare the class inside our geneerated contract.py doc

        this function is not currently used. Instead, class definition is now done in libsimba.class_converter
        """
        converterFunction = """
        def class_to_dict_converter_helper(self, class_dict, attr_name, attr_value):
            if hasattr(attr_value, '__dict__'):
                class_dict[attr_name] = attr_value.__dict__
                for att_name, att_val in class_dict[attr_name].items():
                    self.param_converter_helper(class_dict[attr_name], att_name, att_val)
    
        def class_to_dict_converter(self):
            for att_name, att_value in self.__dict__.items():
                self.param_converter_helper(self.__dict__, att_name, att_value)"""
        converterFunction.replace('\t', '    ')
        converterFunction = converterFunction.rstrip()
        return converterFunction

    def component_default_value(self, component_type:str, def_val: str):
        if component_type == 'int' and def_val == None:
            def_val = 0
        if component_type == 'str' and def_val == None:
            def_val = ''
        if component_type.startswith('List') and def_val == None:
            def_val = []
        return def_val

    def struct_init_signature_with_components(self, struct:str, assignments: List):
        className = self.struct_names[struct]
        sig = f'class {className}(ClassToDictConverter):\n\t\tdef __init__(self'
        components = self.contract['types'][struct]['components']
        for component in components:
            name = component['name']
            assignments.append(f"self.{name}={name}")
            compType = self.native_python_type(component, forward_reference=True)
            # all components will have default value, even if None
            # if we want to change this, then we'll need to move
            # defaulted components to end of components list, since 
            # Python doesn't allow positional arguments to follow keyword arguments
            defaultValue = component.get('default_value', None)
            # the following logic is to mimic solidity default behavior
            defaultValue = self.component_default_value(compType, defaultValue)
            if compType in self.struct_names:
                sig += f', {name}: "{compType}"' # we're handling forward referencing here, which requires quotes 
            else:
                sig += f", {name}: {compType}"
            if compType == 'str':
                sig += f" = '{defaultValue}'"
            else:
                sig += f" = {defaultValue}"
        sig += '):'
        return [sig, assignments]

    def classes_from_structs(self):
        classStrings = []
        for struct in self.contract['types']:
            assignments = []
            sig, assignments = self.struct_init_signature_with_components(struct, assignments)   
            for assigned in assignments:
                sig += f"\n\t\t\t{assigned}"
            sig = sig.replace('\t', '    ')
            classStrings.append(sig)
        return classStrings
    
    def get_dimensions(self, param:str, dims:Optional[int] = 0) -> int:
        """
        Recursive function to determine dimensions of array type

        Args:
            param (str): string formatted parameter (eg 'str[][]')
            dims (Optional[int], optional): [description]. Defaults to 0.

        Returns:
            [int]: number of dimensions in array
        """
        if '[' not in param:
            return dims 
        param = param[param.find('[')+1:]
        dims += 1 
        return self.get_dimensions(param, dims)

    def native_python_type(self, param: dict, forward_reference: bool = False) -> str:
        """
        native_python_type will return a native Python type (int, str, etc.)

        Args:
            param (dict): method parameter for which we want to obtain a native Python data type hint

        Returns:
            (str): string that represents either an array of form List[typ] or typ, where typ is a native python data type
        """
        fullType = param['type']
        if fullType.startswith('struct'):
            # since API expects dict for struct, we pass 'dict' instead of 'object' as a type hint
            fullType = fullType[7:]
            if self.is_array(fullType):
                brackets = fullType[fullType.find('['):]
                structType = self.handle_struct(fullType, forward_reference=forward_reference)
                fullType = structType + brackets
                arrType = self.handle_array(fullType, structType)
                return arrType 
            else:
                structType = self.handle_struct(fullType)
            return structType
        if fullType.startswith('int') or fullType.startswith('uint'):
            basicType = 'int'
            if self.is_array(fullType):
                arrType = self.handle_array(fullType, basicType)
                return arrType
            return basicType
        # will need to add more exhaustive logic for other solidityType -> string conversions here
        # presumably for datetime, etc.
        if fullType.startswith('string') or fullType.startswith('address'):
            basicType = 'str'
            if self.is_array(fullType):
                arrType = self.handle_array(fullType, basicType)
                return arrType
            return basicType
        if fullType.startswith('number'):
            basicType = 'Union[int, float]'
            if self.is_array(fullType):
                arrType = self.handle_array(fullType, basicType)
                return arrType
            return basicType
        if fullType.startswith('bool'):
            basicType = 'bool'
            if self.is_array(fullType):
                arrType = self.handle_array(fullType, basicType)
                return arrType
            return basicType

        # handle cases not handled above - probably need to add some additional logic here
        basicType = fullType
        if self.is_array(fullType):
            arrType = self.handle_array(fullType, basicType)
            return arrType
        return fullType

    def array_restrictions(self, arr:str):
        arr_lengths = {}
        for i in range(self.get_dimensions(arr)):
            arr_len = arr[arr.find('[')+1:arr.find(']')]
            arr_lengths[i] = int(arr_len) if arr_len else None 
            arr = arr[arr.find(']')+1:]
        return arr_lengths

    def check_array_lengths(self, arr:List[Any], param_name, param_restrictions_dict:Dict, level=0):
        level_restriction = param_restrictions_dict[param_name][level]
        if level_restriction is not None:
            if len(arr) != level_restriction:
                raise ValueError("array length error")
        level += 1
        for i, sub_element in enumerate(arr):
            # first check to make sure that if one element is list, all elements are lists
            if i > 0 and type(arr[i]) != type(arr[i-1]):
                raise TypeError("array element types do not match")
            # then recursively check each sublist
            if type(sub_element) == list:
                self.check_array_lengths(sub_element, param_name, param_restrictions_dict, level=level)
            else:
                if param_restrictions_dict[param_name]['contains_uint'] is True:
                    if type(sub_element) != int:
                        raise TypeError("final sub array elements must be type int") 
                    if sub_element < 0:
                        raise ValueError("final sub array elements must be non-negative")
        return True

    def check_uint_restriction(self, param_value):
        if param_value < 0:
            raise ValueError("parameter value must be >= 0")
        if type(param_value) != int:
            raise ValueError("parameter must be type int")
        
    def validate_params(self, method_name, inputs):
        paramRestrictions = self.param_restrictions()
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
                self.check_array_lengths(param_value, param_name, array_params)
        return True

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
            [dict]: example return for a contract with methods 'an_arr', 'array_params', and 'bbb':

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

    def sig_and_input_for_method(self, methodName:str, acceptsFiles:bool, itReturns:bool) -> list:
        params = self.contract_methods[methodName]['params']
        signature = f"def {methodName}(self,"
        inputs = 'inputs= {\n\t'
        for param in params:
            paramName = param['name']
            # we shouldn't include a parameter in our call as _bundleHash
            # we should simply include files in our call:
            if paramName == '_bundleHash':
                continue
            hint_type = self.native_python_type(param, forward_reference=True)
            if hint_type in self.struct_names:
                signature += f' {paramName}: "{hint_type}",'
            else:
                signature += f" {paramName}: {hint_type},"
            inputs += f"\t\t'{paramName}': {paramName},"
            inputs += '\n\t'
        signature = signature[:-1]
        if acceptsFiles:
            signature += ', files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None'
        else:
            signature += ', async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False'
        if itReturns:
            signature += ') -> List[Any]:'
        else:
            signature += '):'
        inputs = inputs.rstrip()
        inputs += '\n\t\t}'
        return [signature, inputs]

    def sig_doc_input_return(self) -> List[str]:
        """
        sig_doc_input_return will return a list of list(zip) form, with the three items in that 
        zipped list being a list of method signatures, method body inputs, and method return statements
        for each method in our contract

        NOTE: in this method, once we reach the logic section of 'if accepts_files', we handle two
        different cases. If the method accepts files, then we allow the developer to specify whether
        the method they are calling is async or not. 
            (ie, we invoke either submit_contract_method_with_files or submit_contract_method_with_files_async
            from https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py)
        
        If the method does not accept files, then
        we allow the developer to specify whether they want to invoke the method, or query invocations
        of the method. 
            (ie, we invoke either submit_method or query_method
            from https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py) 

        Returns:
            sigInputReturn List[str]: list of list(zip) form, with the four items in that 
        zipped list being lists of: method signatures, docStrings, method body inputs, and method return statements
        for all methods in our contract
        """
        signatureDetails = []
        inputDetails = []
        returnDetails = []
        docStringDetails = []
        for methodName in self.contract_methods:
            acceptsFiles = False
            if self.accepts_files(methodName):
                acceptsFiles = True
                docStringDetails.append(f'\t"""\n\t\tIf async_method == True, then {methodName} will be invoked as async, otherwise {methodName} will be invoked as non async\n\t\t"""')
            else:
                docStringDetails.append(f'\t"""\n\t\tIf query_method == True, then invocations of {methodName} will be queried. Otherwise {methodName} will be invoked with inputs.\n\t\t"""')
            itReturns = self.return_data_types(methodName, as_dict=False)
            signature, inputs = self.sig_and_input_for_method(methodName, acceptsFiles, itReturns)
            signatureDetails.append(signature)
            inputDetails.append(inputs)
            if acceptsFiles:
                returnDetails.append(f'if async_method:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files_async("{methodName}", inputs, files=files, opts=opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files("{methodName}", inputs, files=files, opts=opts)')
            else:
                returnDetails.append(f'if query_method:\n\t\t\treturn self.simba_contract.query_method("{methodName}", opts=opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_method("{methodName}", inputs, opts=opts, async_method=async_method)')
        sigDocInputReturn = list(zip(signatureDetails, docStringDetails, inputDetails, returnDetails))
        return sigDocInputReturn

    def write_contract(self):
        """
        write_contract will use a jinja template to create a .py formatted version of our 
        smart contract, for which our contract will be represented as a class
        """
        file_loader = FileSystemLoader(self.template_folder)
        env = Environment(loader=file_loader)
        template = env.get_template(self.contract_template)
        output = template.render(SimbaHintedContractObj=self)
        # following line is to avoid mixing spaces and tabs
        output = output.replace('\t', '    ')
        with open(self.output_file, 'w') as f:
            f.write(output)

