from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files


class DMVImplementationM8:
    def __init__(self):
        self.app_name = "titles"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "DMVImplementationM8"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    class Counter(ClassToDictConverter):
        def __init__(self, _value: int = 0):
            self._value=_value
    
    class Set(ClassToDictConverter):
        def __init__(self, _values: List[bytes] = [], _indexes: Dict = None):
            self._values=_values
            self._indexes=_indexes
    
    class UintSet(ClassToDictConverter):
        def __init__(self, _inner: "DMVImplementationM8.Set" = None):
            self._inner=_inner
    
    class RoleData(ClassToDictConverter):
        def __init__(self, members: Dict = None, adminRole: bytes = None):
            self.members=members
            self.adminRole=adminRole
    
    class AddressSet(ClassToDictConverter):
        def __init__(self, _inner: "DMVImplementationM8.Set" = None):
            self._inner=_inner
    
    class Bytes32Set(ClassToDictConverter):
        def __init__(self, _inner: "DMVImplementationM8.Set" = None):
            self._inner=_inner
    
    class OnChainMetadata(ClassToDictConverter):
        def __init__(self, name: bytes = None, contentHash: bytes = None, description: List[bytes] = [], image: List[bytes] = [], imageHash: bytes = None, exists: bool = None):
            self.name=name
            self.contentHash=contentHash
            self.description=description
            self.image=image
            self.imageHash=imageHash
            self.exists=exists
    
    class OnChainMetadata(ClassToDictConverter):
        def __init__(self, name: bytes = None, contentHash: bytes = None, description: List[bytes] = [], image: List[bytes] = [], imageHash: bytes = None, salvage: bool = None, exists: bool = None):
            self.name=name
            self.contentHash=contentHash
            self.description=description
            self.image=image
            self.imageHash=imageHash
            self.salvage=salvage
            self.exists=exists
    
    class OnChainMetadata(ClassToDictConverter):
        def __init__(self, name: bytes = None, contentHash: bytes = None, description: List[bytes] = [], image: List[bytes] = [], imageHash: bytes = None, exists: bool = None):
            self.name=name
            self.contentHash=contentHash
            self.description=description
            self.image=image
            self.imageHash=imageHash
            self.exists=exists
    
    class OnChainMetadata(ClassToDictConverter):
        def __init__(self, name: bytes = None, contentHash: bytes = None, description: List[bytes] = [], image: List[bytes] = [], imageHash: bytes = None, exists: bool = None):
            self.name=name
            self.contentHash=contentHash
            self.description=description
            self.image=image
            self.imageHash=imageHash
            self.exists=exists
    
    def get_bundle_file(self, bundle_hash, file_name, opts: Optional[dict] = None):
        return self.simba.get_bundle_file(self.app_name, self.contract_name, bundle_hash, file_name, opts)

    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.validate_bundle_hash(bundle_hash, opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def getVIN(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getVIN will be queried. Otherwise getVIN will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getVIN", opts)
        else:
            return self.simba_contract.submit_method("getVIN", inputs, opts, async_method)

    def burnCar(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of burnCar will be queried. Otherwise burnCar will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("burnCar", opts)
        else:
            return self.simba_contract.submit_method("burnCar", inputs, opts, async_method)

    def burnTitle(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of burnTitle will be queried. Otherwise burnTitle will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("burnTitle", opts)
        else:
            return self.simba_contract.submit_method("burnTitle", inputs, opts, async_method)

    def createCar(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createCar will be queried. Otherwise createCar will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createCar", opts)
        else:
            return self.simba_contract.submit_method("createCar", inputs, opts, async_method)

    def createTitle(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, salvage: bool, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createTitle will be queried. Otherwise createTitle will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
            'salvage': salvage,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createTitle", opts)
        else:
            return self.simba_contract.submit_method("createTitle", inputs, opts, async_method)

    def transferCar(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of transferCar will be queried. Otherwise transferCar will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("transferCar", opts)
        else:
            return self.simba_contract.submit_method("transferCar", inputs, opts, async_method)

    def transferTitle(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of transferTitle will be queried. Otherwise transferTitle will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("transferTitle", opts)
        else:
            return self.simba_contract.submit_method("transferTitle", inputs, opts, async_method)

    def getCarMetadata(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getCarMetadata will be queried. Otherwise getCarMetadata will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getCarMetadata", opts)
        else:
            return self.simba_contract.submit_method("getCarMetadata", inputs, opts, async_method)

    def updateCarImage(self, tokenId: int, image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of updateCarImage will be queried. Otherwise updateCarImage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("updateCarImage", opts)
        else:
            return self.simba_contract.submit_method("updateCarImage", inputs, opts, async_method)

    def burnRegistration(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of burnRegistration will be queried. Otherwise burnRegistration will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("burnRegistration", opts)
        else:
            return self.simba_contract.submit_method("burnRegistration", inputs, opts, async_method)

    def getTitleMetadata(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getTitleMetadata will be queried. Otherwise getTitleMetadata will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getTitleMetadata", opts)
        else:
            return self.simba_contract.submit_method("getTitleMetadata", inputs, opts, async_method)

    def updateTitleImage(self, tokenId: int, image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of updateTitleImage will be queried. Otherwise updateTitleImage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("updateTitleImage", opts)
        else:
            return self.simba_contract.submit_method("updateTitleImage", inputs, opts, async_method)

    def createRegistration(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createRegistration will be queried. Otherwise createRegistration will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createRegistration", opts)
        else:
            return self.simba_contract.submit_method("createRegistration", inputs, opts, async_method)

    def createSalvageTitle(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createSalvageTitle will be queried. Otherwise createSalvageTitle will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createSalvageTitle", opts)
        else:
            return self.simba_contract.submit_method("createSalvageTitle", inputs, opts, async_method)

    def getTitleDocumentID(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getTitleDocumentID will be queried. Otherwise getTitleDocumentID will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getTitleDocumentID", opts)
        else:
            return self.simba_contract.submit_method("getTitleDocumentID", inputs, opts, async_method)

    def transferRegistration(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of transferRegistration will be queried. Otherwise transferRegistration will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("transferRegistration", opts)
        else:
            return self.simba_contract.submit_method("transferRegistration", inputs, opts, async_method)

    def createNonSalvageTitle(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createNonSalvageTitle will be queried. Otherwise createNonSalvageTitle will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createNonSalvageTitle", opts)
        else:
            return self.simba_contract.submit_method("createNonSalvageTitle", inputs, opts, async_method)

    def getRegistrationMetadata(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getRegistrationMetadata will be queried. Otherwise getRegistrationMetadata will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getRegistrationMetadata", opts)
        else:
            return self.simba_contract.submit_method("getRegistrationMetadata", inputs, opts, async_method)

    def updateRegistrationImage(self, tokenId: int, image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of updateRegistrationImage will be queried. Otherwise updateRegistrationImage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("updateRegistrationImage", opts)
        else:
            return self.simba_contract.submit_method("updateRegistrationImage", inputs, opts, async_method)

    def burnCertificateOfSalvage(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of burnCertificateOfSalvage will be queried. Otherwise burnCertificateOfSalvage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("burnCertificateOfSalvage", opts)
        else:
            return self.simba_contract.submit_method("burnCertificateOfSalvage", inputs, opts, async_method)

    def getRegistrationDocumentID(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getRegistrationDocumentID will be queried. Otherwise getRegistrationDocumentID will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getRegistrationDocumentID", opts)
        else:
            return self.simba_contract.submit_method("getRegistrationDocumentID", inputs, opts, async_method)

    def createCertificateOfSalvage(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of createCertificateOfSalvage will be queried. Otherwise createCertificateOfSalvage will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
            'contentHash': contentHash,
            'name': name,
            'description': description,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("createCertificateOfSalvage", opts)
        else:
            return self.simba_contract.submit_method("createCertificateOfSalvage", inputs, opts, async_method)

    def transferCertificateOfSalvage(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of transferCertificateOfSalvage will be queried. Otherwise transferCertificateOfSalvage will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("transferCertificateOfSalvage", opts)
        else:
            return self.simba_contract.submit_method("transferCertificateOfSalvage", inputs, opts, async_method)

    def getCertificateOfSalvageMetadata(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getCertificateOfSalvageMetadata will be queried. Otherwise getCertificateOfSalvageMetadata will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getCertificateOfSalvageMetadata", opts)
        else:
            return self.simba_contract.submit_method("getCertificateOfSalvageMetadata", inputs, opts, async_method)

    def updateCertificateOfSalvageImage(self, tokenId: int, image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of updateCertificateOfSalvageImage will be queried. Otherwise updateCertificateOfSalvageImage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("updateCertificateOfSalvageImage", opts)
        else:
            return self.simba_contract.submit_method("updateCertificateOfSalvageImage", inputs, opts, async_method)

    def getCertificateOfSalvageDocumentID(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getCertificateOfSalvageDocumentID will be queried. Otherwise getCertificateOfSalvageDocumentID will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getCertificateOfSalvageDocumentID", opts)
        else:
            return self.simba_contract.submit_method("getCertificateOfSalvageDocumentID", inputs, opts, async_method)
