import libsimba
from libsimba.simba import Simba
from datetime import datetime
from typing import List, Tuple, Dict, String, Any, Optional

class Application:
    def __init__(self):
        self.app_name = "app_md_2_app"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "Application"
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
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def types(self, __MyAsset: str, myText: str, myEmail: str, myUid: str, myDecimal: str, myBigInteger: int, myInteger: int, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of types will be queried. Otherwise types will be invoked with inputs.
        """
        inputs= {
            '__MyAsset': __MyAsset,
            'myText': myText,
            'myEmail': myEmail,
            'myUid': myUid,
            'myDecimal': myDecimal,
            'myBigInteger': myBigInteger,
            'myInteger': myInteger,
        }
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        if query_method:
            return self.simba_contract.query_method("types", opts=opts)
        else:
            return self.simba_contract.submit_method("types", inputs, opts=opts, async_method=async_method)

    def types1(self, myDate: str, myDateTime: str, myMoney: str, myURL: str, myAddress: str, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of types1 will be queried. Otherwise types1 will be invoked with inputs.
        """
        inputs= {
            'myDate': myDate,
            'myDateTime': myDateTime,
            'myMoney': myMoney,
            'myURL': myURL,
            'myAddress': myAddress,
        }
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        if query_method:
            return self.simba_contract.query_method("types1", opts=opts)
        else:
            return self.simba_contract.submit_method("types1", inputs, opts=opts, async_method=async_method)
