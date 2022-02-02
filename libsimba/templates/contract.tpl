from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from libsimba.utils import SearchFilter

class {{SimbaHintedContractObj.contract_class_name}}:
    def __init__(self):
        self.app_name = "{{SimbaHintedContractObj.app_name}}"
        self.base_api_url = "{{SimbaHintedContractObj.base_api_url}}"
        self.contract_name = "{{SimbaHintedContractObj.contract_name}}"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.smart_contract_client(self.app_name, self.contract_name)
    {% for cls in SimbaHintedContractObj.classes_from_structs() %}
    {{cls}}
    {% endfor %}
{% for signature, docString, inputs, returnDetails in SimbaHintedContractObj.sig_doc_input_return() %}
    {{signature}}
    {{docString}}
        {{inputs}}
        convert_classes(inputs)
        {{returnDetails}}
{% endfor %}