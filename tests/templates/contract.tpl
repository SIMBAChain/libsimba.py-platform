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
    
    class ConverterBase:
    {{- SimbaHintedContractObj.convert_classes_to_dicts_nested() }}
    {% for cls in SimbaHintedContractObj.classes_from_structs() %}
    {{cls}}
    {% endfor %}
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)
{% for signature, docString, inputs, returnDetails in SimbaHintedContractObj.sig_doc_input_return() %}
    {{signature}}
    {{docString}}
        {{inputs}}
        # the following logic converts classes, including nested classes, back to dicts for our API calls
        for attr_name, attr_value in inputs.items():
            if hasattr(attr_value, "convert_params"):
                attr_value.convert_params()
                inputs[attr_name] = attr_value.__dict__
        
        {{returnDetails}}
{% endfor %}