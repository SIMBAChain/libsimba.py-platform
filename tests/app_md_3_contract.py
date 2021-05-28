import libsimba
from libsimba.simba import Simba
from datetime import datetime
from typing import List, Tuple, Dict, String, Any, Optional

class AssemblyBom:
    def __init__(self):
        self.app_name = "app_md_3_app"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "AssemblyBom"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    class Part:
        def __init__(self, __Part: str = ''):
            self.__Part=__Part
    
    class Assembly:
        def __init__(self, __Assembly: str = ''):
            self.__Assembly=__Assembly
    
    class Supplier:
        def __init__(self, __Supplier: str = ''):
            self.__Supplier=__Supplier
    
    class StockItem:
        def __init__(self, __StockItem: str = '', part: libsimba.AssemblyBom.Part = None, unitOfIssue: str = '', SMRCode: str = '', NSN: str = '', partNumber: str = '', UOC: str = ''):
            self.__StockItem=__StockItem
            self.part=part
            self.unitOfIssue=unitOfIssue
            self.SMRCode=SMRCode
            self.NSN=NSN
            self.partNumber=partNumber
            self.UOC=UOC
    
    class AssemblyPart:
        def __init__(self, __AssemblyPart: str = '', part: libsimba.AssemblyBom.Part = None, quantity: str = ''):
            self.__AssemblyPart=__AssemblyPart
            self.part=part
            self.quantity=quantity
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def mbomStock(self, stockItem: libsimba.AssemblyBom.StockItem, specifiedSupplier: libsimba.AssemblyBom.Supplier, SOH: str, remanufacturedCost: str, totalCost: str, comment: str, point50LikeItems: str, pc_Replacement_8716_15_EA: str, pc_Replacement_Q667_600_EA: str, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of mbomStock will be queried. Otherwise mbomStock will be invoked with inputs.
        """
        inputs= {
            'stockItem': stockItem,
            'specifiedSupplier': specifiedSupplier,
            'SOH': SOH,
            'remanufacturedCost': remanufacturedCost,
            'totalCost': totalCost,
            'comment': comment,
            'point50LikeItems': point50LikeItems,
            'pc_Replacement_8716_15_EA': pc_Replacement_8716_15_EA,
            'pc_Replacement_Q667_600_EA': pc_Replacement_Q667_600_EA,
        }
        if query_method:
            return self.simba_contract.query_method("mbomStock", opts=opts)
        else:
            return self.simba_contract.submit_method("mbomStock", inputs, opts=opts, async_method=async_method)

    def assemblage(self, name: libsimba.AssemblyBom.Assembly, niins: List[libsimba.AssemblyBom.Part], parts: List[libsimba.AssemblyBom.AssemblyPart], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of assemblage will be queried. Otherwise assemblage will be invoked with inputs.
        """
        inputs= {
            'name': name,
            'niins': niins,
            'parts': parts,
        }
        if query_method:
            return self.simba_contract.query_method("assemblage", opts=opts)
        else:
            return self.simba_contract.submit_method("assemblage", inputs, opts=opts, async_method=async_method)

    def assemblyGroup(self, name: libsimba.AssemblyBom.Assembly, subAssemblies: List[libsimba.AssemblyBom.Assembly], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of assemblyGroup will be queried. Otherwise assemblyGroup will be invoked with inputs.
        """
        inputs= {
            'name': name,
            'subAssemblies': subAssemblies,
        }
        if query_method:
            return self.simba_contract.query_method("assemblyGroup", opts=opts)
        else:
            return self.simba_contract.submit_method("assemblyGroup", inputs, opts=opts, async_method=async_method)
