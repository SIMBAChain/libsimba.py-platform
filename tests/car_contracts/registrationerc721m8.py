from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from context import Context
from accesscontrolenumerable import AccessControlEnumerable
from erc721enumerable import ERC721Enumerable
from erc721burnable import ERC721Burnable
from erc721pausable import ERC721Pausable
from iaccesscontrolenumerable import IAccessControlEnumerable
from accesscontrol import AccessControl
from iaccesscontrol import IAccessControl
from erc165 import ERC165
from ierc165 import IERC165
from erc721 import ERC721
from ierc721enumerable import IERC721Enumerable
from ierc721 import IERC721
from ierc721metadata import IERC721Metadata
from pausable import Pausable


class RegistrationERC721M8(Context,AccessControlEnumerable,ERC721Enumerable,ERC721Burnable,ERC721Pausable,IAccessControlEnumerable,AccessControl,IAccessControl,ERC165,IERC165,ERC721,IERC721Enumerable,IERC721,IERC721Metadata,Pausable):
    def __init__(self):
        self.app_name = "titles"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "CarERC721M8"
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
        def __init__(self, _inner: "CarERC721M8.Set" = None):
            self._inner=_inner
    
    class RoleData(ClassToDictConverter):
        def __init__(self, members: Dict = None, adminRole: bytes = None):
            self.members=members
            self.adminRole=adminRole
    
    class AddressSet(ClassToDictConverter):
        def __init__(self, _inner: "CarERC721M8.Set" = None):
            self._inner=_inner
    
    class Bytes32Set(ClassToDictConverter):
        def __init__(self, _inner: "CarERC721M8.Set" = None):
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

    def burn(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of burn will be queried. Otherwise burn will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("burn", opts)
        else:
            return self.simba_contract.submit_method("burn", inputs, opts, async_method)

    def mint(self, to: str, tokenId: int, contentHash: bytes, name: bytes, description: List[bytes], image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of mint will be queried. Otherwise mint will be invoked with inputs.
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
            return self.simba_contract.query_method("mint", opts)
        else:
            return self.simba_contract.submit_method("mint", inputs, opts, async_method)

    def name(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of name will be queried. Otherwise name will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("name", opts)
        else:
            return self.simba_contract.submit_method("name", inputs, opts, async_method)

    def pause(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of pause will be queried. Otherwise pause will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("pause", opts)
        else:
            return self.simba_contract.submit_method("pause", inputs, opts, async_method)

    def paused(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of paused will be queried. Otherwise paused will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("paused", opts)
        else:
            return self.simba_contract.submit_method("paused", inputs, opts, async_method)

    def symbol(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of symbol will be queried. Otherwise symbol will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("symbol", opts)
        else:
            return self.simba_contract.submit_method("symbol", inputs, opts, async_method)

    def approve(self, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of approve will be queried. Otherwise approve will be invoked with inputs.
        """
        inputs= {
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("approve", opts)
        else:
            return self.simba_contract.submit_method("approve", inputs, opts, async_method)

    def getName(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getName will be queried. Otherwise getName will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getName", opts)
        else:
            return self.simba_contract.submit_method("getName", inputs, opts, async_method)

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

    def ownerOf(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of ownerOf will be queried. Otherwise ownerOf will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("ownerOf", opts)
        else:
            return self.simba_contract.submit_method("ownerOf", inputs, opts, async_method)

    def unpause(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of unpause will be queried. Otherwise unpause will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("unpause", opts)
        else:
            return self.simba_contract.submit_method("unpause", inputs, opts, async_method)

    def tokenURI(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of tokenURI will be queried. Otherwise tokenURI will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("tokenURI", opts)
        else:
            return self.simba_contract.submit_method("tokenURI", inputs, opts, async_method)

    def balanceOf(self, owner: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of balanceOf will be queried. Otherwise balanceOf will be invoked with inputs.
        """
        inputs= {
            'owner': owner,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("balanceOf", opts)
        else:
            return self.simba_contract.submit_method("balanceOf", inputs, opts, async_method)

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

    def getApproved(self, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of getApproved will be queried. Otherwise getApproved will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("getApproved", opts)
        else:
            return self.simba_contract.submit_method("getApproved", inputs, opts, async_method)

    def totalSupply(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of totalSupply will be queried. Otherwise totalSupply will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("totalSupply", opts)
        else:
            return self.simba_contract.submit_method("totalSupply", inputs, opts, async_method)

    def updateImage(self, tokenId: int, image: List[bytes], imageHash: bytes, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of updateImage will be queried. Otherwise updateImage will be invoked with inputs.
        """
        inputs= {
            'tokenId': tokenId,
            'image': image,
            'imageHash': imageHash,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("updateImage", opts)
        else:
            return self.simba_contract.submit_method("updateImage", inputs, opts, async_method)

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

    def tokenByIndex(self, index: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of tokenByIndex will be queried. Otherwise tokenByIndex will be invoked with inputs.
        """
        inputs= {
            'index': index,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("tokenByIndex", opts)
        else:
            return self.simba_contract.submit_method("tokenByIndex", inputs, opts, async_method)

    def transferFrom(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of transferFrom will be queried. Otherwise transferFrom will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("transferFrom", opts)
        else:
            return self.simba_contract.submit_method("transferFrom", inputs, opts, async_method)

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

    def isApprovedForAll(self, owner: str, operator: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of isApprovedForAll will be queried. Otherwise isApprovedForAll will be invoked with inputs.
        """
        inputs= {
            'owner': owner,
            'operator': operator,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("isApprovedForAll", opts)
        else:
            return self.simba_contract.submit_method("isApprovedForAll", inputs, opts, async_method)

    def safeTransferFrom(self, fromParam: str, to: str, tokenId: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of safeTransferFrom will be queried. Otherwise safeTransferFrom will be invoked with inputs.
        """
        inputs= {
            'from': fromParam,
            'to': to,
            'tokenId': tokenId,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("safeTransferFrom", opts)
        else:
            return self.simba_contract.submit_method("safeTransferFrom", inputs, opts, async_method)

    def setApprovalForAll(self, operator: str, approved: bool, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of setApprovalForAll will be queried. Otherwise setApprovalForAll will be invoked with inputs.
        """
        inputs= {
            'operator': operator,
            'approved': approved,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("setApprovalForAll", opts)
        else:
            return self.simba_contract.submit_method("setApprovalForAll", inputs, opts, async_method)

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

    def tokenOfOwnerByIndex(self, owner: str, index: int, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False) -> List[Any]:
        """
        If query_method == True, then invocations of tokenOfOwnerByIndex will be queried. Otherwise tokenOfOwnerByIndex will be invoked with inputs.
        """
        inputs= {
            'owner': owner,
            'index': index,
        }
        convert_classes(inputs)
        if query_method:
            return self.simba_contract.query_method("tokenOfOwnerByIndex", opts)
        else:
            return self.simba_contract.submit_method("tokenOfOwnerByIndex", inputs, opts, async_method)
