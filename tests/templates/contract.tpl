import libsimba
from libsimba.simba import Simba
from datetime import datetime
from typing import List, Tuple, Dict, String, Any, Optional

class {{SimbaHintedContractObj.contract_name}}:
    def __init__(self):
        self.app_name = "{{SimbaHintedContractObj.app_name}}"
        self.base_api_url = "{{SimbaHintedContractObj.base_api_url}}"
        self.contract_name = "{{SimbaHintedContractObj.contract_name}}"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)
{% for signature, docString, inputs, returnDetails in SimbaHintedContractObj.sigInputReturnDetails() %}
    {{signature}}
    {{docString}}
        {{inputs}}
        {{returnDetails}}
{% endfor %}