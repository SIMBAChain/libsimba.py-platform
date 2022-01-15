from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from accesscontrolenumerable import AccessControlEnumerable
from iaccesscontrolenumerable import IAccessControlEnumerable
from accesscontrol import AccessControl
from iaccesscontrol import IAccessControl
from context import Context
from erc165 import ERC165
from ierc165 import IERC165


class DMVUpgradableM8(AccessControlEnumerable,IAccessControlEnumerable,AccessControl,IAccessControl,Context,ERC165,IERC165):
    def __init__(self):
        self.app_name = "titles"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "DMVUpgradableM8"
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
        def __init__(self, _inner: "DMVUpgradableM8.Set" = None):
            self._inner=_inner
    
    class RoleData(ClassToDictConverter):
        def __init__(self, members: Dict = None, adminRole: bytes = None):
            self.members=members
            self.adminRole=adminRole
    
    class AddressSet(ClassToDictConverter):
        def __init__(self, _inner: "DMVUpgradableM8.Set" = None):
            self._inner=_inner
    
    class Bytes32Set(ClassToDictConverter):
        def __init__(self, _inner: "DMVUpgradableM8.Set" = None):
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

    def init(self, _dmvInterface: str, _dmvImpl: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of init will be queried. Otherwise init will be invoked with inputs.
        """
        inputs= {
            '_dmvInterface': _dmvInterface,
            '_dmvImpl': _dmvImpl,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("init", opts)
        else:
            return self.simba_contract.submit_method("init", inputs, opts, async_method)

    def hasRole(self, role: bytes, account: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of hasRole will be queried. Otherwise hasRole will be invoked with inputs.
        """
        inputs= {
            'role': role,
            'account': account,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("hasRole", opts)
        else:
            return self.simba_contract.submit_method("hasRole", inputs, opts, async_method)

    def grantRole(self, role: bytes, account: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of grantRole will be queried. Otherwise grantRole will be invoked with inputs.
        """
        inputs= {
            'role': role,
            'account': account,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("grantRole", opts)
        else:
            return self.simba_contract.submit_method("grantRole", inputs, opts, async_method)

    def getDMVImpl(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getDMVImpl will be queried. Otherwise getDMVImpl will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getDMVImpl", opts)
        else:
            return self.simba_contract.submit_method("getDMVImpl", inputs, opts, async_method)

    def revokeRole(self, role: bytes, account: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of revokeRole will be queried. Otherwise revokeRole will be invoked with inputs.
        """
        inputs= {
            'role': role,
            'account': account,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("revokeRole", opts)
        else:
            return self.simba_contract.submit_method("revokeRole", inputs, opts, async_method)

    def getRoleAdmin(self, role: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getRoleAdmin will be queried. Otherwise getRoleAdmin will be invoked with inputs.
        """
        inputs= {
            'role': role,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getRoleAdmin", opts)
        else:
            return self.simba_contract.submit_method("getRoleAdmin", inputs, opts, async_method)

    def renounceRole(self, role: bytes, account: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of renounceRole will be queried. Otherwise renounceRole will be invoked with inputs.
        """
        inputs= {
            'role': role,
            'account': account,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("renounceRole", opts)
        else:
            return self.simba_contract.submit_method("renounceRole", inputs, opts, async_method)

    def getRoleMember(self, role: bytes, index: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getRoleMember will be queried. Otherwise getRoleMember will be invoked with inputs.
        """
        inputs= {
            'role': role,
            'index': index,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getRoleMember", opts)
        else:
            return self.simba_contract.submit_method("getRoleMember", inputs, opts, async_method)

    def getDMVInterface(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getDMVInterface will be queried. Otherwise getDMVInterface will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getDMVInterface", opts)
        else:
            return self.simba_contract.submit_method("getDMVInterface", inputs, opts, async_method)

    def confirmImplChange(self, _proposedImpl: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of confirmImplChange will be queried. Otherwise confirmImplChange will be invoked with inputs.
        """
        inputs= {
            '_proposedImpl': _proposedImpl,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("confirmImplChange", opts)
        else:
            return self.simba_contract.submit_method("confirmImplChange", inputs, opts, async_method)

    def supportsInterface(self, interfaceId: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of supportsInterface will be queried. Otherwise supportsInterface will be invoked with inputs.
        """
        inputs= {
            'interfaceId': interfaceId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("supportsInterface", opts)
        else:
            return self.simba_contract.submit_method("supportsInterface", inputs, opts, async_method)

    def getRoleMemberCount(self, role: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getRoleMemberCount will be queried. Otherwise getRoleMemberCount will be invoked with inputs.
        """
        inputs= {
            'role': role,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getRoleMemberCount", opts)
        else:
            return self.simba_contract.submit_method("getRoleMemberCount", inputs, opts, async_method)

    def confirmInterfaceChange(self, _proposedInterface: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of confirmInterfaceChange will be queried. Otherwise confirmInterfaceChange will be invoked with inputs.
        """
        inputs= {
            '_proposedInterface': _proposedInterface,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("confirmInterfaceChange", opts)
        else:
            return self.simba_contract.submit_method("confirmInterfaceChange", inputs, opts, async_method)
