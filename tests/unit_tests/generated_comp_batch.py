import libsimba
from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes

class newCompBatch:
    def __init__(self):
        self.app_name = "newCompBatch"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "newCompBatch"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def batch_number(self, batch_name: str, item_count: int, datetime: int, __batch_number: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of batch_number will be queried. Otherwise batch_number will be invoked with inputs.
        """
        inputs= {
            'batch_name': batch_name,
            'item_count': item_count,
            'datetime': datetime,
            '__batch_number': __batch_number,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("batch_number", opts)
        else:
            return self.simba_contract.submit_method("batch_number", inputs, opts, async_method)

    def request_for_initialization(self, datetime: int, __batch_number: str, files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then request_for_initialization will be invoked as async, otherwise request_for_initialization will be invoked as non async
        """
        inputs= {
            'datetime': datetime,
            '__batch_number': __batch_number,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("request_for_initialization", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("request_for_initialization", inputs, files, opts)

    def send_endpoint_texture_profile(self, __batch_number: str, files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then send_endpoint_texture_profile will be invoked as async, otherwise send_endpoint_texture_profile will be invoked as non async
        """
        inputs= {
            '__batch_number': __batch_number,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("send_endpoint_texture_profile", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("send_endpoint_texture_profile", inputs, files, opts)

    def request_for_inspection_profile(self, datetime: int, __batch_number: str, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of request_for_inspection_profile will be queried. Otherwise request_for_inspection_profile will be invoked with inputs.
        """
        inputs= {
            'datetime': datetime,
            '__batch_number': __batch_number,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("request_for_inspection_profile", opts)
        else:
            return self.simba_contract.submit_method("request_for_inspection_profile", inputs, opts, async_method)

    def send_inspection_profile_to_nde(self, __batch_number: str, files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then send_inspection_profile_to_nde will be invoked as async, otherwise send_inspection_profile_to_nde will be invoked as non async
        """
        inputs= {
            '__batch_number': __batch_number,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("send_inspection_profile_to_nde", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("send_inspection_profile_to_nde", inputs, files, opts)
