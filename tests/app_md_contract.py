import libsimba
from libsimba.simba import Simba
from datetime import datetime
from typing import List, Tuple, Dict, String, Any, Optional

class Application:
    def __init__(self):
        self.app_name = "app_md_app"
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

    def a_str_arr(self, first: List[str], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of a_str_arr will be queried. Otherwise a_str_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("a_str_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("a_str_arr", inputs, opts=opts)

    def an_arr(self, first: List[int], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of an_arr will be queried. Otherwise an_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("an_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("an_arr", inputs, opts=opts)

    def two_arrs(self, first: List[int], second: List[int], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of two_arrs will be queried. Otherwise two_arrs will be invoked with inputs.
        """
        inputs= {
            'first': first,
            'second': second,
        }
        if query_method:
            return self.simba_contract.query_method("two_arrs", opts=opts)
        else:
            return self.simba_contract.submit_method("two_arrs", inputs, opts=opts)

    def address_arr(self, first: List[str], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of address_arr will be queried. Otherwise address_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("address_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("address_arr", inputs, opts=opts)

    def bbb(self, first: List[List[int]], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of bbb will be queried. Otherwise bbb will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("bbb", opts=opts)
        else:
            return self.simba_contract.submit_method("bbb", inputs, opts=opts)

    def nested_arr(self, first: List[List[int]], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr will be queried. Otherwise nested_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("nested_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr", inputs, opts=opts)

    def nested_arr_2(self, first: List[List[int]], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr_2 will be queried. Otherwise nested_arr_2 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("nested_arr_2", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr_2", inputs, opts=opts)

    def nested_arr_3(self, first: List[List[int]], opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr_3 will be queried. Otherwise nested_arr_3 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        if query_method:
            return self.simba_contract.query_method("nested_arr_3", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr_3", inputs, opts=opts)

    def nested_arr_4(self, first: List[List[int]], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then nested_arr_4 will be invoked as async, otherwise nested_arr_4 will be invoked as non async
        """
        inputs= {
            'first': first,
        }
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("nested_arr_4", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("nested_arr_4", inputs, files=files, opts=opts)

    def structTest_1(self, people: List[dict], test_bool: bool, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of structTest_1 will be queried. Otherwise structTest_1 will be invoked with inputs.
        """
        inputs= {
            'people': people,
            'test_bool': test_bool,
        }
        if query_method:
            return self.simba_contract.query_method("structTest_1", opts=opts)
        else:
            return self.simba_contract.submit_method("structTest_1", inputs, opts=opts)

    def structTest_2(self, person: dict, test_bool: bool, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of structTest_2 will be queried. Otherwise structTest_2 will be invoked with inputs.
        """
        inputs= {
            'person': person,
            'test_bool': test_bool,
        }
        if query_method:
            return self.simba_contract.query_method("structTest_2", opts=opts)
        else:
            return self.simba_contract.submit_method("structTest_2", inputs, opts=opts)

    def structTest_5(self, person: dict, files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_5 will be invoked as async, otherwise structTest_5 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_5", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_5", inputs, files=files, opts=opts)

    def structTest_3(self, person: dict, files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_3 will be invoked as async, otherwise structTest_3 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_3", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_3", inputs, files=files, opts=opts)

    def structTest_4(self, persons: List[dict], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_4 will be invoked as async, otherwise structTest_4 will be invoked as non async
        """
        inputs= {
            'persons': persons,
        }
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_4", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_4", inputs, files=files, opts=opts)

    def structTest_6(self, persons_0: List[dict], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_6 will be invoked as async, otherwise structTest_6 will be invoked as non async
        """
        inputs= {
            'persons_0': persons_0,
        }
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_6", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_6", inputs, files=files, opts=opts)

    def nowt(self, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nowt will be queried. Otherwise nowt will be invoked with inputs.
        """
        inputs= {
        }
        if query_method:
            return self.simba_contract.query_method("nowt", opts=opts)
        else:
            return self.simba_contract.submit_method("nowt", inputs, opts=opts)

    def date_string(self, the_date: str, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of date_string will be queried. Otherwise date_string will be invoked with inputs.
        """
        inputs= {
            'the_date': the_date,
        }
        if query_method:
            return self.simba_contract.query_method("date_string", opts=opts)
        else:
            return self.simba_contract.submit_method("date_string", inputs, opts=opts)
