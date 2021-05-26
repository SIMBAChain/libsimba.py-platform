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
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def mbomStock(self, stockItem: dict, specifiedSupplier: dict, SOH: str, remanufacturedCost: str, totalCost: str, comment: str, point50LikeItems: str, pc_Replacement_8716_15_EA: str, pc_Replacement_Q667_600_EA: str, opts: Optional[dict] = None, query_method: bool = False):
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
            return self.simba_contract.submit_method("mbomStock", inputs, opts=opts)

    def assemblage(self, name: dict, niins: List[dict], parts: List[dict], opts: Optional[dict] = None, query_method: bool = False):
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
            return self.simba_contract.submit_method("assemblage", inputs, opts=opts)

    def assemblyGroup(self, name: dict, subAssemblies: List[dict], opts: Optional[dict] = None, query_method: bool = False):
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
            return self.simba_contract.submit_method("assemblyGroup", inputs, opts=opts)
