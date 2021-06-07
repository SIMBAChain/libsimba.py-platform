
from typing import List, Tuple, Dict, Optional, Union, Any
from jinja2 import Environment, FileSystemLoader 
import requests
from libsimba.decorators import auth_required
from libsimba.utils import build_url

class SimbaHintedContract:
    def __init__(
        self, 
        app_name: str, 
        contract_name: str, 
        base_api_url: str = 'https://api.sep.dev.simbachain.com/',
        contract_template: str ='contract.tpl', 
        output_file: str = 'newContract.py',
        template_folder: str ='templates',
        ):
        """
        SimbaHintedContract allows us to represent our smart contract as a Python class
        The purpose of this class is largely to provide an SDK that utilizes type hinting 
        and exposes method calls instead of python get requests
        Note that the underlying functionality is still contained in https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py

        Args:
            metadata (str): string formatted json metadata from our smart contract
            app_name (str): name of the app that accesses our smart contract
            base_api_url (str, optional): Defaults to 'https://api.sep.dev.simbachain.com/'.
            contract_template (str, optional): name of the jinja template used to create .py version of contract code. Defaults to 'contract.tpl'.
            output_file (str, optional): name of .py file we wish to write our .py version of contract to. Defaults to 'newContract.py'.
            template_folder (str, optional): folder contianing our jinja template. Defaults to 'templates'.
        """
        self.app_name = app_name
        self.contract_name = contract_name
        self.base_api_url = base_api_url
        self.contract_uri = "{}/contract/{}".format(self.app_name, self.contract_name)
        self.async_contract_uri = "{}/async/contract/{}".format(self.app_name, self.contract_name)
        self.metadata = self.get_metadata()
        self.contract = self.metadata['contract']
        # note that we have to specify the following line, because the contract name passed by the user 
        # and used for the API may be different than what's specified in the actual contract, and what 
        # we actually want to use here is the contract name found in the metadata
        self.contract_name_from_metadata = self.contract['name']
        self.contract_methods = self.contract['methods']
        self.contract_template = contract_template 
        self.output_file = output_file
        self.template_folder = template_folder
        self.struct_names = {fullName: fullName.split('.')[1] for fullName in self.contract.get('types', {})}
        self.write_contract()

    @auth_required 
    def get_metadata(self, headers, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/?format=json".format(self.contract_uri), opts) 
        resp = requests.get(url, headers=headers)
        metadata = resp.json()['metadata']
        return metadata
    
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
            nativeType = self.hinted_data_type(r)
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
            paramType (str): native Python type obtained in hinted_data_type (int, str, etc.)

        Returns:
            arrType (str): string formatted version of array or nested array
        """
        arrType = f'List[{basicType}]'
        for _ in range(self.get_dimensions(fullType)-1):
            arrType = f'List[{arrType}]'
        return arrType

    def is_array(self, param):
        return param.endswith(']')

    def handle_struct(self, structParam: str, forward_reference:bool = True):
        """
        gives us custom struct type, accounting for array

        Args:
            structParam (str): struct in either Contract.Struct or Contract.Struct[]...[] format

        Returns:
            [str]: string in either 'libsimba.Contract.Struct' or 'List[libsimba.Contract.Struct]'form
        """
        if self.is_array(structParam):
            structType = structParam[:structParam.find('[')]
            newStructType = structType.split('.')[1]
            newStructType = self.contract_name + '.' + newStructType 
            structType = newStructType
            if forward_reference:
                structType = f'"{structType}"'
            return structType

        newStructType = structParam.split('.')[1]
        newStructType = self.contract_name + '.' + newStructType 
        structType = newStructType

        if forward_reference:
            structType = f'"{structType}"'
        else:
            structType = structType
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
        if component_type == 'int' and def_val == None:
            def_val = 0
        if component_type == 'str' and def_val == None:
            def_val = ''
        if component_type.startswith('List') and def_val == None:
            def_val = []
        return def_val

    def struct_init_signature_with_components(self, struct:str):
        """
        struct_init_signature_with_components will produce a signature for the __init__
        method for our classes that represent structs, with parameters (components) and default values

        Args:
            struct (str): name of struct that we want to create a class object for

        Returns:
            [str, list]: list containing a signature and attribute assignments for struct class
        """
        assignments = []
        className = self.struct_names[struct]
        sig = f'class {className}(ClassToDictConverter):\n\t\tdef __init__(self'
        structs = self.contract.get('types', {})
        if not structs:
            return
        else:
            components = structs[struct]['components']
        for component in components:
            name = component['name']
            assignments.append(f"self.{name}={name}")
            compType = self.hinted_data_type(component, forward_reference=True)
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
        """
        generates class object strings for each of our contract's structs

        Returns:
            [List[str]]: list of string representations of struct classes
        """
        classStrings = []
        structs = self.contract.get('types', {})
        for struct in structs:
            sig, assignments = self.struct_init_signature_with_components(struct)   
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

    def hinted_data_type(self, param: dict, forward_reference: bool = True) -> str:
        """
        hinted_data_type will return a type for type hinting. This may be a native python 
        data type, or may be a custom data type representing a struct

        Args:
            param (dict): method parameter for which we want to obtain a native Python data type hint
            forward_reference (bool): if True, then we return our data type inside quotes.
                We do this as a forward reference, in cases where we are referencing a data type
                that is not yet recovnized by the the interpreter (eg a custom class type)
        
        Returns:
            (str): string that represents either an array of form List[typ] or typ, where typ is a native python data type
        """
        fullType = param['type']
        if fullType.startswith('struct'):
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

    def sig_and_input_for_method(self, methodName:str, acceptsFiles:bool, itReturns:bool) -> list:
        """
        generate a method signature, along with a dictionary of inputs, for a contract method

        Args:
            methodName (str): contract method name
            acceptsFiles (bool): bool that specifies whether a method accepts files
            itReturns (bool): bool that specifies whether a method has a return value

        Returns:
            [str, str]: list containing [method signature, method input dict as string]
        """
        params = self.contract_methods[methodName]['params']
        signature = f"def {methodName}(self,"
        inputs = 'inputs= {\n\t'
        for param in params:
            paramName = param['name']
            # we shouldn't include a parameter in our call as _bundleHash
            # we should simply include files in our call:
            if paramName == '_bundleHash':
                continue
            hint_type = self.hinted_data_type(param, forward_reference=True)
            if hint_type in self.struct_names:
                signature += f' {paramName}: "{hint_type}",'
            else:
                signature += f" {paramName}: {hint_type},"
            inputs += f"\t\t'{paramName}': {paramName},"
            inputs += '\n\t'
        signature = signature[:-1]
        if acceptsFiles:
            signature += ', files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None'
        else:
            signature += ', async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False'
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
                returnDetails.append(f'if async_method:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files_async("{methodName}", inputs, files, opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files("{methodName}", inputs, files, opts)')
            else:
                returnDetails.append(f'if query_method:\n\t\t\treturn self.simba_contract.query_method("{methodName}", opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_method("{methodName}", inputs, opts, async_method)')
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



