import libsimba
from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes

class {{SimbaHintedContractObj.contract_name}}:
    def __init__(self):
        self.app_name = "{{SimbaHintedContractObj.app_name}}"
        self.base_api_url = "{{SimbaHintedContractObj.base_api_url}}"
        self.contract_name = "{{SimbaHintedContractObj.contract_name}}"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    {% for cls in SimbaHintedContractObj.classes_from_structs() %}
    {{cls}}
    {% endfor %}
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)
{% for signature, docString, inputs, returnDetails in SimbaHintedContractObj.sig_doc_input_return() %}
    {{signature}}
    {{docString}}
        {{inputs}}
        convert_classes(inputs)
        
        {{returnDetails}}
{% endfor %}