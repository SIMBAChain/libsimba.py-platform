import libsimba
from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes

class TestSimbaHinted:
    def __init__(self):
        self.app_name = "TestSimbaHinted"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "TestSimbaHinted"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    class Addr(ClassToDictConverter):
        def __init__(self, street: str = '', number: int = 0, town: str = ''):
            self.street=street
            self.number=number
            self.town=town
    
    class Person(ClassToDictConverter):
        def __init__(self, name: str = '', age: int = 0, addr: "TestSimbaHinted.Addr" = None):
            self.name=name
            self.age=age
            self.addr=addr
    
    class AddressPerson(ClassToDictConverter):
        def __init__(self, name: str = '', age: int = 0, addrs: List["TestSimbaHinted.Addr"] = []):
            self.name=name
            self.age=age
            self.addrs=addrs
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def nowt(self, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of nowt will be queried. Otherwise nowt will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nowt", opts)
        else:
            return self.simba_contract.submit_method("nowt", inputs, opts, async_method)

    def an_arr(self, first: List[int], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of an_arr will be queried. Otherwise an_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("an_arr", opts)
        else:
            return self.simba_contract.submit_method("an_arr", inputs, opts, async_method)

    def two_arrs(self, first: List[int], second: List[int], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of two_arrs will be queried. Otherwise two_arrs will be invoked with inputs.
        """
        inputs= {
            'first': first,
            'second': second,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("two_arrs", opts)
        else:
            return self.simba_contract.submit_method("two_arrs", inputs, opts, async_method)

    def address_arr(self, first: List[str], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of address_arr will be queried. Otherwise address_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("address_arr", opts)
        else:
            return self.simba_contract.submit_method("address_arr", inputs, opts, async_method)

    def nested_arr_0(self, first: List[List[int]], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of nested_arr_0 will be queried. Otherwise nested_arr_0 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_0", opts)
        else:
            return self.simba_contract.submit_method("nested_arr_0", inputs, opts, async_method)

    def nested_arr_1(self, first: List[List[int]], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of nested_arr_1 will be queried. Otherwise nested_arr_1 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_1", opts)
        else:
            return self.simba_contract.submit_method("nested_arr_1", inputs, opts, async_method)

    def nested_arr_2(self, first: List[List[int]], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of nested_arr_2 will be queried. Otherwise nested_arr_2 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_2", opts)
        else:
            return self.simba_contract.submit_method("nested_arr_2", inputs, opts, async_method)

    def nested_arr_3(self, first: List[List[int]], async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of nested_arr_3 will be queried. Otherwise nested_arr_3 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_3", opts)
        else:
            return self.simba_contract.submit_method("nested_arr_3", inputs, opts, async_method)

    def nested_arr_4(self, first: List[List[int]], files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then nested_arr_4 will be invoked as async, otherwise nested_arr_4 will be invoked as non async
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("nested_arr_4", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("nested_arr_4", inputs, files, opts)

    def structTest_1(self, people: List["TestSimbaHinted.Person"], test_bool: bool, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of structTest_1 will be queried. Otherwise structTest_1 will be invoked with inputs.
        """
        inputs= {
            'people': people,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("structTest_1", opts)
        else:
            return self.simba_contract.submit_method("structTest_1", inputs, opts, async_method)

    def structTest_2(self, person: "TestSimbaHinted.Person", test_bool: bool, async_method: Optional[bool] = False, opts: Optional[dict] = None, query_method: Optional[bool] = False):
        """
        If query_method == True, then invocations of structTest_2 will be queried. Otherwise structTest_2 will be invoked with inputs.
        """
        inputs= {
            'person': person,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("structTest_2", opts)
        else:
            return self.simba_contract.submit_method("structTest_2", inputs, opts, async_method)

    def structTest_3(self, person: "TestSimbaHinted.AddressPerson", files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_3 will be invoked as async, otherwise structTest_3 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_3", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_3", inputs, files, opts)

    def structTest_4(self, persons: List["TestSimbaHinted.AddressPerson"], files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_4 will be invoked as async, otherwise structTest_4 will be invoked as non async
        """
        inputs= {
            'persons': persons,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_4", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_4", inputs, files, opts)

    def structTest_5(self, person: "TestSimbaHinted.Person", files: List[Tuple], async_method: Optional[bool] = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_5 will be invoked as async, otherwise structTest_5 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_5", inputs, files, opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_5", inputs, files, opts)
