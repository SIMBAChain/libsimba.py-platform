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
    
    class ConverterBase:
        def param_converter_helper(self, class_dict, attr_name, attr_value):
            if hasattr(attr_value, '__dict__'):
                class_dict[attr_name] = attr_value.__dict__
                for att_name, att_val in class_dict[attr_name].items():
                    self.param_converter_helper(class_dict[attr_name], att_name, att_val)
    
        def convert_params(self):
            for att_name, att_value in self.__dict__.items():
                self.param_converter_helper(self.__dict__, att_name, att_value)
    
    class Part(ConverterBase):
        def __init__(self, __Part: str = ''):
            self.__Part=__Part
    
    class Assembly(ConverterBase):
        def __init__(self, __Assembly: str = ''):
            self.__Assembly=__Assembly
    
    class Supplier(ConverterBase):
        def __init__(self, __Supplier: str = ''):
            self.__Supplier=__Supplier
    
    class StockItem(ConverterBase):
        def __init__(self, __StockItem: str = '', part: "AssemblyBom.Part" = None, unitOfIssue: str = '', SMRCode: str = '', NSN: str = '', partNumber: str = '', UOC: str = ''):
            self.__StockItem=__StockItem
            self.part=part
            self.unitOfIssue=unitOfIssue
            self.SMRCode=SMRCode
            self.NSN=NSN
            self.partNumber=partNumber
            self.UOC=UOC
    
    class AssemblyPart(ConverterBase):
        def __init__(self, __AssemblyPart: str = '', part: "AssemblyBom.Part" = None, quantity: str = ''):
            self.__AssemblyPart=__AssemblyPart
            self.part=part
            self.quantity=quantity
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def mbomStock(self, stockItem: "AssemblyBom.StockItem", specifiedSupplier: "AssemblyBom.Supplier", SOH: str, remanufacturedCost: str, totalCost: str, comment: str, point50LikeItems: str, pc_Replacement_8716_15_EA: str, pc_Replacement_Q667_600_EA: str, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
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
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        if query_method:
            return self.simba_contract.query_method("mbomStock", opts=opts)
        else:
            return self.simba_contract.submit_method("mbomStock", inputs, opts=opts, async_method=async_method)

    def assemblage(self, name: "AssemblyBom.Assembly", niins: List["AssemblyBom.Part"], parts: List["AssemblyBom.AssemblyPart"], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of assemblage will be queried. Otherwise assemblage will be invoked with inputs.
        """
        inputs= {
            'name': name,
            'niins': niins,
            'parts': parts,
        }
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        if query_method:
            return self.simba_contract.query_method("assemblage", opts=opts)
        else:
            return self.simba_contract.submit_method("assemblage", inputs, opts=opts, async_method=async_method)

    def assemblyGroup(self, name: "AssemblyBom.Assembly", subAssemblies: List["AssemblyBom.Assembly"], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of assemblyGroup will be queried. Otherwise assemblyGroup will be invoked with inputs.
        """
        inputs= {
            'name': name,
            'subAssemblies': subAssemblies,
        }
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        if query_method:
            return self.simba_contract.query_method("assemblyGroup", opts=opts)
        else:
            return self.simba_contract.submit_method("assemblyGroup", inputs, opts=opts, async_method=async_method)
