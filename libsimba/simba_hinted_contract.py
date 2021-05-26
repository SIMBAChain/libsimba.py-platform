
import pprint 
pprint = pprint.PrettyPrinter().pprint
from typing import List, Tuple, Dict, Optional, Union, Any
import json 
from jinja2 import Environment, FileSystemLoader 


class SimbaHintedContract:
    def __init__(
        self, 
        metaData: str, 
        appName: str, 
        baseAPIurl: str = 'https://api.sep.dev.simbachain.com/',
        contractTemplate: str ='contract.tpl', 
        outputFile: str = 'newContract.py',
        templateFolder: str ='templates'
        ):
        """
        SimbaHintedContract allows us to represent our smart contract as a Python class
        The purpose of this class is largely to provide an SDK that utilizes type hinting 
        and method calls (as opposed to python requests)
        Note that the underlying functionality is still contained in https://github.com/SIMBAChain/libsimba.py-platform/blob/main/libsimba/simba_contract.py

        Args:
            metaData (str): string formatted json metadata from our smart contract
            appName (str): name of the app that accesses our smart contract
            baseAPIurl (str, optional): Defaults to 'https://api.sep.dev.simbachain.com/'.
            contractTemplate (str, optional): name of the jinja template used to create .py version of contract code. Defaults to 'contract.tpl'.
            outputFile (str, optional): name of .py file we wish to write our .py version of contract to. Defaults to 'newContract.py'.
            templateFolder (str, optional): folder contianing our jinja template. Defaults to 'templates'.
        """
        metadata = open(metaData, 'r')
        metadata = json.load(metadata)
        self.contract = metadata['contract']
        self.contract_name = self.contract['name']
        self.contract_methods = self.contract['methods']
        self.app_name = appName
        self.base_api_url = baseAPIurl
        self.contract_template = contractTemplate 
        self.output_file = outputFile
        self.template_folder = templateFolder
    
    def contractStructs(self) -> List[Any]:
        """
        contractStructs returns a list of struct types from our contract

        Returns:
            List[Any]: list of struct types from contract
        """
        return [struct for struct in self.metadata_object.contract.types]
    
    def acceptsFiles(self, method_name:str) -> bool:
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
    
    def fileMethods(self) -> List[str]:
        """
        returns a list of method names that accept files. 
        
        Not currently used.

        Returns:
            List[str]: list of contract methods that accept files
        """
        return [method for method in self.contract_methods if self.acceptsFiles(method)]

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
            nativeType = self.nativePythonType(r)
            if as_dict:
                result[str(i)] = nativeType
            else:
                result.append(nativeType)
        return result

    def handleArray(self, fullType:str, basicType:str) -> str:
        """
        handleArray is meant to handle arrays and nested arrays, and return a string formatted version of that nested array

        Args:
            param (app_metadata.DataType): method parameter, of type DataType, for which we want to obtain a native Python data type hint
            paramType (str): native Python type obtained in nativePythonType (int, str, etc.)

        Returns:
            arrType (str): string formatted version of array or nested array
        """
        arrType = f'List[{basicType}]'
        for _ in range(self.getDimensions(fullType)-1):
            arrType = f'List[{arrType}]'
        return arrType

    def isArray(self, param):
        return param.endswith(']')
    
    def getDimensions(self, param:str, dims:Optional[int] = 0) -> int:
        """
        Recursive function to determine dimensions of array type

        Args:
            param (str): string formatted parameter (eg 'str[][][]')
            dims (Optional[int], optional): [description]. Defaults to 0.

        Returns:
            [int]: number of dimensions in array
        """
        if '[' not in param:
            return dims 
        param = param[param.find('[')+1:]
        dims += 1 
        return self.getDimensions(param, dims)

    def nativePythonType(self, param: dict) -> str:
        """
        nativePythonType will return a native Python type (int, str, etc.)

        Args:
            param (dict): method parameter for which we want to obtain a native Python data type hint

        Returns:
            (str): string that represents either an array of form List[typ] or typ, where typ is a native python data type
        """
        fullType = param['type']
        if fullType.startswith('struct'):
            # since API expects dict for struct, we pass 'dict' instead of 'object' as a type hint
            basicType = 'dict'
            if self.isArray(fullType):
                arrType = self.handleArray(fullType, basicType)
                return arrType 
            return basicType
        if fullType.startswith('int') or fullType.startswith('uint'):
            basicType = 'int'
            if self.isArray(fullType):
                arrType = self.handleArray(fullType, basicType)
                return arrType
            return basicType
        if fullType.startswith('string') or fullType.startswith('address'):
            basicType = 'str'
            if self.isArray(fullType):
                arrType = self.handleArray(fullType, basicType)
                return arrType
            return basicType
        if fullType.startswith('number'):
            basicType = 'Union[int, float]'
            if self.isArray(fullType):
                arrType = self.handleArray(fullType, basicType)
                return arrType
            return basicType
        if fullType.startswith('bool'):
            basicType = 'bool'
            if self.isArray(fullType):
                arrType = self.handleArray(fullType, basicType)
                return arrType
            return basicType

        # handle cases not handled above - probably need to add some additional logic here
        basicType = fullType
        if self.isArray(fullType):
            arrType = self.handleArray(fullType, basicType)
            return arrType
        return fullType

    def sigInputReturnDetails(self) -> List[str]:
        """
        sigInputReturnDetails will return a list of list(zip) form, with the three items in that 
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
            accepts_files = False
            if self.acceptsFiles(methodName):
                accepts_files = True
                docStringDetails.append(f'\t"""\n\t\tIf async_method == True, then {methodName} will be invoked as async, otherwise {methodName} will be invoked as non async\n\t\t"""')
            else:
                docStringDetails.append(f'\t"""\n\t\tIf query_method == True, then invocations of {methodName} will be queried. Otherwise {methodName} will be invoked with inputs.\n\t\t"""')
            itReturns = self.return_data_types(methodName, as_dict=False)
            params = self.contract_methods[methodName]['params']
            signature = f"def {methodName}(self,"
            inputs = 'inputs= {\n\t'
            for param in params:
                paramName = param['name']
                # we shouldn't include a parameter in our call as _bundleHash
                # we should simply include files in our call:
                if paramName == '_bundleHash':
                    continue
                hint_type = self.nativePythonType(param)
                signature += f" {paramName}: {hint_type},"
                inputs += f"\t\t'{paramName}': {paramName},"
                inputs += '\n\t'
            signature = signature[:-1]
            if accepts_files:
                signature += ', files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None'
            else:
                signature += ', opts: Optional[dict] = None, query_method: bool = False'
            if itReturns:
                signature += ') -> List[Any]:'
            else:
                signature += '):'
            inputs = inputs.rstrip()
            inputs += '\n\t\t}'
            signatureDetails.append(signature)
            inputDetails.append(inputs)
            if accepts_files:
                returnDetails.append(f'if async_method:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files_async("{methodName}", inputs, files=files, opts=opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_contract_method_with_files("{methodName}", inputs, files=files, opts=opts)')
            else:
                returnDetails.append(f'if query_method:\n\t\t\treturn self.simba_contract.query_method("{methodName}", opts=opts)\n\t\telse:\n\t\t\treturn self.simba_contract.submit_method("{methodName}", inputs, opts=opts)')
        sigInputReturn = list(zip(signatureDetails, docStringDetails, inputDetails, returnDetails))
        return sigInputReturn

    def writeContract(self):
        """
        writeContract will use a jinja template to create a .py formatted version of our 
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

