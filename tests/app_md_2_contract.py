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
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def types(self, __MyAsset: str, myText: str, myEmail: str, myUid: str, myDecimal: str, myBigInteger: int, myInteger: int, opts: Optional[dict] = None, query_method: bool = False):
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
        if query_method:
            return self.simba_contract.query_method("types", opts=opts)
        else:
            return self.simba_contract.submit_method("types", inputs, opts=opts)

    def types1(self, myDate: str, myDateTime: str, myMoney: str, myURL: str, myAddress: str, opts: Optional[dict] = None, query_method: bool = False):
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
        if query_method:
            return self.simba_contract.query_method("types1", opts=opts)
        else:
            return self.simba_contract.submit_method("types1", inputs, opts=opts)
