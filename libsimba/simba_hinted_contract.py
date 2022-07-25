from typing import List, Dict, Optional, Union, Any
from bleach import clean
from jinja2 import Template
import requests
from libsimba.settings import BASE_API_URL
from libsimba.decorators import auth_required
from libsimba.utils import build_url
from libsimba import templates
import importlib.resources
import re
from libsimba.keyword_converter import KeywordConverter
from libsimba.simba_sync import SimbaSync
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class SimbaHintedContract:
    def __init__(
        self, 
        app_name: str, 
        contract_name: str = None,
        contract_class_name: str = None,
        template_name: str = 'py_contract.tpl',
        base_api_url: str = BASE_API_URL,
        output_file: str = None,
        language: str = "python"
        ):
        """
        SimbaHintedContract allows us to represent our smart contract as a Python class
        Smart contract methods will be exposed as class methods, and smart contract structs 
        will be represented as subclasses of our contract class
        Note that the underlying functionality for method calls is still contained in https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py
        Args:
            app_name (str): name of the app that accesses our smart contract
            base_api_url (str, optional): Defaults to {BASE_API_URL}.
            output_file (str, optional): name of .py file we wish to write our .py version of contract to. Defaults to 'newContract.py'.
            contract_class_name (str, optional): if we want our python class representation of our contract to have a different name 
                than contract_name, then we specify it with this parameter
        """
        log.debug(f' :: ENTER : ')
        self.app_name = app_name
        self.language = language
        self.contract_name = contract_name
        self.contract_class_name = contract_class_name or contract_name[0].upper() + contract_name[1:]
        self.validate_class_name(self.contract_class_name)
        self.base_api_url = base_api_url
        self.contract_uri = "{}/contract/{}".format(self.app_name, self.contract_name)
        self.sync_contract_uri = "{}/sync/contract/{}".format(self.app_name, self.contract_name)
        self.metadata = self.get_metadata()
        self.contract = self.metadata['contract']
        self.contract_methods = self.contract['methods']
        self.output_file = output_file or f'{self.contract_name}.py'
        self.struct_names = {fullName: fullName.split('.')[1] for fullName in self.contract.get('types', {})}
        self.keyword_converter = KeywordConverter(language = self.language)
        self.template_name = template_name

    @classmethod
    def write_all_contracts(cls, app_name: str):
        """
        class method for writing Python versions of all deployed contracts for app {app_name}

        Args:
            app_name (str): name of the app. This method will create Python versions of all
                deployed smart contracts for that app
        """
        log.debug(f' :: ENTER :')
        all_contracts = cls._get_all_deployed_contracts_for_app(app_name)
        for contract in all_contracts:
            contract_name = contract['asset_type']
            shc = SimbaHintedContract(app_name, contract_name=contract_name)
            shc.write_contract()

    def write_contract(self):
        """
        write_contract will use a jinja template to create a .py formatted version of our 
        smart contract, for which our contract will be represented as a class
        """
        log.debug(f' :: ENTER :')
        tmplt = importlib.resources.read_text(templates, self.template_name)
        template = Template(tmplt)
        output = template.render(SimbaHintedContractObj=self)
        # following line is to avoid mixing spaces and tabs
        output = output.replace('\t', '    ')
        log.info(f':: simba : writing {self.contract_name} to {self.output_file}')
        with open(self.output_file, 'w') as f:
            f.write(output)
        log.debug(f' :: EXIT :')

    @classmethod
    def _get_all_deployed_contracts_for_app(cls, app_name: str):
        log.debug(f' :: ENTER :')
        simba_sync = SimbaSync()
        resp = simba_sync.list_contracts(app_name)
        contracts = resp
        return contracts


    @auth_required 
    def get_metadata(self, headers, opts: Optional[dict] = None):
        params = {
            "headers": headers,
            "opts": opts,
        }
        log.debug(f' :: ENTER : params : {params}')
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/?format=json".format(self.contract_uri), opts) 
        resp = requests.get(url, headers=headers)
        metadata = resp.json()['metadata']
        for item in metadata['contract']:
            log.debug(f'{item}: {metadata["contract"][item]}\n\n')
        log.debug(f' :: EXIT : metadata : {metadata}')
        return metadata

    def validate_class_name(self, class_name:str):
        """
        validates name we wish to give our contract class object
        Args:
            class_name ([type]): [description]
        Raises:
            ValueError: if class_name begins with a digit
            ValueError: if class_name contains nonalpha or non_underscore
        """
        params = {
            "class_name": class_name,
        }
        log.debug(f' :: ENTER : params : {params}')
        if class_name[0].isdigit():
            log.error(f' :: ERROR : Class name cannot begin with a digit')
            raise ValueError("validate_class_name: Class name cannot begin with a digit")
        match = re.search('[^0-9a-zA-Z_]', class_name)
        if match is not None:
            error_message = "Class Name can only contain alphanumeric chars and underscores"
            log.error(f' :: EXIT : {error_message}')
            raise ValueError(f'validate_class_name: {error_message}')
    
    def accepts_files(self, method_name:str) -> bool:
        """
        returns a bool indicating whether method_name accepts files or not, as indicated by whether
        _bundleHash is present as a parameter name in method_name's parameters
        Args:
            method_name (str): method_name for which we want to determine if files are accepted or not
        Returns:
            bool: 
        """
        params = {
            "method_name": method_name,
        }
        log.debug(f' :: ENTER : params : {params}')
        for param in self.contract_methods[method_name]['params']:
            if param['name'] == '_bundleHash':
                log.debug(f' :: EXIT : True')
                return True 
        log.debug(f' :: EXIT : False')
        return False

    def is_accessor(self, method_name:str) -> bool:
        """
        returns a bool indicating whether method_name is an accessor (getter)
        Args:
            method_name (str): method_name for which we want to determine if files are accepted or not
        Returns:
            bool: 
        """
        params = {
            "method_name": method_name,
        }
        log.debug(f': :: ENTER : params : {params}')
        _is_accessor = self.contract_methods[method_name]['accessor']
        log.debug(f' :: EXIT : _is_accessor : ${_is_accessor}')
        return _is_accessor
    
    def file_methods(self) -> List[str]:
        """
        returns a list of method names that accept files. 
        
        Not currently used.

        Returns:
            List[str]: list of contract methods that accept files
        """
        log.debug(f' :: ENTER :')
        f_methods = [method for method in self.contract_methods if self.accepts_files(method)]
        log.debug(f' :: EXIT : f_methods : {f_methods}')
        return f_methods

    def return_data_types(self, method_name:str, as_dict=False) -> Union[List, Dict]:
        """
        get the native Python data types for return values from contract methods

        Not currently used, since what we're actually returning is usually http response objects

        Args:
            method_name (str): method_name to obtain return data type for
            as_dict (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        params = {
            "method_name": method_name,
            "as_dict": as_dict,
        }
        log.debug(f' :: ENTER : params : {params}')
        m = self.contract_methods.get(method_name, None)
        if as_dict:
            result = {}
        else:
            result = []
        if not m:
            log.debug(f' :: EXIT : no file methods')
            return None
        for i, r in enumerate(m.get('returns', [])):
            dt = r['type'] # come back and handle type later
            native_type = self.hinted_data_type(r)
            if as_dict:
                result[str(i)] = native_type
            else:
                result.append(native_type)
        log.debug(f' :: EXIT : m : {m}')
        return result

    def handle_array(self, full_type: str, basic_type: str) -> str:
        """
        handle_array is meant to handle arrays and nested arrays, and return a string formatted version of that nested array
        
        Args:
            param (app_metadata.DataType): method parameter, of type DataType, for which we want to obtain a native Python data type hint
            paramType (str): native Python type obtained in hinted_data_type (int, str, etc.)
        
        Returns:
            arr_type (str): string formatted version of array or nested array
        """
        params = {
            "full_type": full_type,
            "basic_type": basic_type,
        }
        log.debug(f' :: ENTER : params : {params}')
        arr_type = f'List[{basic_type}]'
        for _ in range(self.get_dimensions(full_type)-1):
            arr_type = f'List[{arr_type}]'
        log.debug(f' :: EXIT : arr_type : {arr_type}')
        return arr_type

    def is_array(self, param) -> bool:
        """
        is_array uses regex to determine whether a param ends with brackets enclosing any
        number of digits

        Args:
            param (_type_): string version of param, eg uint256[][4]

        Returns:
            bool: self-explanatory
        """
        params = {
            "param": param,
        }
        log.debug(f' :: ENTER : params : {params}')
        pattern = re.compile("^[0-9a-z-A-Z.\[\]]*\[[0-9]*\]$")
        is_an_array = pattern.match(param) != None
        log.debug(f' :: EXIT : is_an_array : {is_an_array}')
        return is_an_array

    def handle_struct(self, struct_param: str, forward_reference:bool = True):
        """
        gives us custom struct type, accounting for array
        Args:
            struct_param (str): struct in either Contract.Struct or Contract.Struct[]...[] format
        Returns:
            [str]: string in either 'libsimba.Contract.Struct' or 'List[libsimba.Contract.Struct]'form
        """
        params = {
            "struct_param": struct_param,
            "forward_reference": forward_reference,
        }
        log.debug(f' :: ENTER : params : {params}')
        if self.is_array(struct_param):
            struct_type = struct_param[:struct_param.find('[')]
            new_struct_type = struct_type.split('.')[1]
            new_struct_type = self.contract_class_name + '.' + new_struct_type 
            struct_type = new_struct_type
            if forward_reference:
                struct_type = f'"{struct_type}"'
            log.debug(f' :: EXIT : struct_type : {struct_type}')
            return struct_type

        new_struct_type = struct_param.split('.')[1]
        new_struct_type = self.contract_class_name + '.' + new_struct_type 
        struct_type = new_struct_type

        if forward_reference:
            struct_type = f'"{struct_type}"'
        log.debug(f' :: EXIT : struct_type : {struct_type}')
        return struct_type

    def component_default_value(self, component_type:str, def_val: Any = None):
        """
        All classes that we use to represent classes should default to empty values
        for their respective data types, to mimic solidity behavior
        Args:
            component_type (str): string representing data type ('int', 'str', etc.)
            def_val (str): default value that should be assigned to variable of component_type. Detafults to None.
        Returns:
            [Any]: default value for component_type
        """
        params = {
            "component_type": component_type,
            "def_val": def_val,
        }
        log.debug(f' :: ENTER : params : {params}')
        # # Until a reason for returning default values other than None
        # # is discovered we will return None
        # if component_type == 'int' and def_val == None:
        #     def_val = 0
        # if component_type == 'str' and def_val == None:
        #     def_val = ''
        # if component_type.startswith('List') and def_val == None:
        #     def_val = []
        # log.debug(f' :: EXIT : def_val : {def_val}')
        # # return None in str form if we don't find a proper default value
        return None

    def struct_class_name_and_components(self, struct:str) -> dict:
        """
        struct_class_name_and_components will return a dict with info on
        struct we wish to represent as a class
        
        Args:
            struct (str): name of struct that we want to create a class object for
        Returns:
            struct_dict: dict : dict containing info for struct we will represent as a class
        """
        params = {
            "struct": struct,
        }
        log.debug(f' :: ENTER : params : {params}')
        struct_dict = {}
        class_name = self.struct_names[struct]
        class_name = self.keyword_converter.convert_keyword(class_name)
        struct_dict["class_name"] = class_name
        structs = self.contract.get('types', {})
        if not structs:
            log.debug(f' :: EXIT : no structs')
            return
        else:
            components = structs[struct]['components']
        struct_dict["components"] = []
        for component in components:
            comp_dict = {}
            name = component['name']
            name = self.keyword_converter.convert_keyword(name)
            comp_dict["comp_name"] = name
            comp_type = self.hinted_data_type(component, forward_reference=True)
            # all components will have default value, even if None
            # if we want to change this, then we'll need to move
            # defaulted components to end of components list, since 
            # Python doesn't allow positional arguments to follow keyword arguments
            default_value = component.get('default_value', None)
            # the following logic is to mimic solidity default behavior
            default_value = self.component_default_value(comp_type, default_value)
            if comp_type in self.struct_names:
                comp_dict["comp_type"] = f'"{comp_type}"'
            else:
                comp_dict["comp_type"] = comp_type
            if comp_type == 'str':
                comp_dict["default_value"] = f'"{default_value}"'
            else:
                comp_dict["default_value"] = default_value
            struct_dict["components"].append(comp_dict)
        log.debug(f' :: EXIT : struct_dict : {struct_dict}')
        # return sig_assignments
        return struct_dict

    def classes_from_structs(self):
        """
        generates class object strings for each of our contract's structs
        Returns:
            [List[dict]]: list of dicts containing info on structs we
            wish to represent as classes
        """
        log.debug(f' :: ENTER :')
        struct_dicts = []
        structs = self.contract.get('types', {})
        for struct in structs:
            struct_dict = self.struct_class_name_and_components(struct)   
            struct_dicts.append(struct_dict)
        return struct_dicts
    
    def get_dimensions(self, param:str, dims:Optional[int] = 0) -> int:
        """
        Recursive function to determine dimensions of array type
        Args:
            param (str): string formatted parameter (eg 'str[][]')
            dims (Optional[int], optional): [description]. Defaults to 0.
        Returns:
            [int]: number of dimensions in array
        """
        params = {
            "param": param,
            "dims": dims,
        }
        log.debug(f' :: ENTER : params : {params}')
        if '[' not in param:
            return dims 
        param = param[param.find('[')+1:]
        dims += 1 
        return self.get_dimensions(param, dims)

    def hinted_data_type(self, param: dict, forward_reference: bool = True) -> str:
        """
        hinted_data_type will return a type for type hinting. This may be a native python 
        data type, or may be a custom data type representing a struct
        Args:
            param (dict): method parameter for which we want to obtain a native Python data type hint
            forward_reference (bool): if True, then we return our data type inside quotes.
                We do this as a forward reference, in cases where we are referencing a data type
                that is not yet recognized by the the interpreter (eg a custom class type, which we used to represent solidity structs)
        
        Returns:
            (str): string that represents either an array of form List[typ] or typ, where typ is a data type
        """
        params = {
            "param": param,
            "forward_reference": forward_reference,
        }
        log.debug(f' :: ENTER : params : {params}')
        full_type = param['type']
        if full_type.startswith('struct'):
            full_type = full_type[7:]
            if self.is_array(full_type):
                brackets = full_type[full_type.find('['):]
                struct_type = self.handle_struct(full_type, forward_reference=forward_reference)
                full_type = struct_type + brackets
                arr_type = self.handle_array(full_type, struct_type)
                return arr_type 
            else:
                struct_type = self.handle_struct(full_type)
            return struct_type
        if full_type.startswith('int') or full_type.startswith('uint'):
            basic_type = 'int'
            if self.is_array(full_type):
                arr_type = self.handle_array(full_type, basic_type)
                return arr_type
            return basic_type
        if full_type.startswith('string') or full_type.startswith('address'):
            basic_type = 'str'
            if self.is_array(full_type):
                arr_type = self.handle_array(full_type, basic_type)
                return arr_type
            return basic_type
        if full_type.startswith('byte'):
            basic_type = 'bytes'
            if self.is_array(full_type):
                arr_type = self.handle_array(full_type, basic_type)
                return arr_type
            return basic_type
        if full_type.startswith('bool'):
            basic_type = 'bool'
            if self.is_array(full_type):
                arr_type = self.handle_array(full_type, basic_type)
                return arr_type
            return basic_type
        # handle cases not handled above - may need to add some additional logic here
        if self.is_array(full_type):
            basic_type = full_type[:full_type.find('[')]
            arr_type = self.handle_array(full_type, basic_type)
            return arr_type
        return full_type

    def method_info(self, method_name:str, accepts_files:bool, it_returns:bool, is_accessor: bool) -> dict:
        """
        method_info produces a dict of info for method
        
        Args:
            method_name (str): contract method name
            accepts_files (bool): bool that specifies whether a method accepts files
            it_returns (bool): bool that specifies whether a method has a return value
        Returns:
            method_dict: list containing [method signature, method input dict as string]
        """
        params = {
            "method_name": method_name,
            "accepts_files": accepts_files,
            "it_returns": it_returns,
        }
        log.debug(f' :: ENTER : params : {params}')
        params = self.contract_methods[method_name]['params']
        method_name = self.keyword_converter.convert_keyword(method_name)
        method_dict = {
            "method_name": method_name,
            "accepts_files": accepts_files,
            "param_info": [],
            "is_accessor": is_accessor,
            }
        for param in params:
            input_dict = {}
            param_name = param['name']
            # the following line obviates collision between datetime module and our datetime parameter
            cleaned_param_name = 'dateTime' if param_name == 'datetime' else param_name
            cleaned_param_name = self.keyword_converter.convert_keyword(cleaned_param_name)
            if param_name == '_bundleHash':
                continue
            hint_type = self.hinted_data_type(param, forward_reference=True)
            default_value = self.component_default_value(hint_type)
            input_dict["param_name"] = cleaned_param_name
            input_dict["original_param_name"] = param_name
            input_dict["default_value"] = default_value
            if hint_type in self.struct_names:
                input_dict["hint_type"] = f"{hint_type}"
            else:
                input_dict["hint_type"] = hint_type
            method_dict['param_info'].append(input_dict)
        log.debug(f' :: EXIT : method_dict : {method_dict}')
        return method_dict

    def info_for_all_methods(self) -> List[dict]:
        """
        info_for_all_methods will return a list of dicts containing info for
        all methods in our contract
        Returns:
            info_for_methods List[dict]: list of dicts containing info for all our
            methods
        """
        log.debug(f' :: ENTER :')
        info_for_methods = []
        for method_name in self.contract_methods:
            accepts_files = self.accepts_files(method_name)
            it_returns = self.return_data_types(method_name, as_dict=False)
            is_accessor = self.is_accessor(method_name)
            info_for_methods.append(self.method_info(method_name, accepts_files, it_returns, is_accessor))
        return info_for_methods
