import libsimba
from libsimba.simba import Simba
from datetime import datetime
from typing import List, Tuple, Dict, String, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes

class Application:
    def __init__(self):
        self.app_name = "app_md_app"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "Application"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.get_contract(self.app_name, self.contract_name)
    
    class Person(ClassToDictConverter):
        def __init__(self, name: str = '2020-01-01T00:00:00.000', age: int = 99, addr: "Application.Addr" = None):
            self.name=name
            self.age=age
            self.addr=addr
    
    class Addr(ClassToDictConverter):
        def __init__(self, street: str = '', number: int = 0, town: str = ''):
            self.street=street
            self.number=number
            self.town=town
    
    class AddressPerson(ClassToDictConverter):
        def __init__(self, name: str = '', age: int = 0, addrs: List["Application.Addr"] = []):
            self.name=name
            self.age=age
            self.addrs=addrs
    
    def get_transactions(self, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(opts=opts)
    
    def validate_bundle_hash(self, bundle_hash: str, opts: Optional[dict] = None):
        return self.simba_contract.get_transactions(bundle_hash, opts=opts)

    def get_transaction_statuses(self, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        return self.simba_contract.get_transaction_statuses(txn_hashes, opts)

    def uint_and_uint_arr_test(self, first_uint: int, a_nested_uint_array: List[List[int]], non_nested_uint_array: List[List[int]], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of uint_and_uint_arr_test will be queried. Otherwise uint_and_uint_arr_test will be invoked with inputs.
        """
        inputs= {
            'first_uint': first_uint,
            'a_nested_uint_array': a_nested_uint_array,
            'non_nested_uint_array': non_nested_uint_array,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("uint_and_uint_arr_test", opts=opts)
        else:
            return self.simba_contract.submit_method("uint_and_uint_arr_test", inputs, opts=opts, async_method=async_method)

    def another_uint_param(self, another_uint: int, second_uint: int, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of another_uint_param will be queried. Otherwise another_uint_param will be invoked with inputs.
        """
        inputs= {
            'another_uint': another_uint,
            'second_uint': second_uint,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("another_uint_param", opts=opts)
        else:
            return self.simba_contract.submit_method("another_uint_param", inputs, opts=opts, async_method=async_method)

    def a_str_arr(self, first: List[str], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of a_str_arr will be queried. Otherwise a_str_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("a_str_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("a_str_arr", inputs, opts=opts, async_method=async_method)

    def an_arr(self, first: List[int], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of an_arr will be queried. Otherwise an_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("an_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("an_arr", inputs, opts=opts, async_method=async_method)

    def two_arrs(self, first: List[int], second: List[int], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of two_arrs will be queried. Otherwise two_arrs will be invoked with inputs.
        """
        inputs= {
            'first': first,
            'second': second,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("two_arrs", opts=opts)
        else:
            return self.simba_contract.submit_method("two_arrs", inputs, opts=opts, async_method=async_method)

    def address_arr(self, first: List[str], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of address_arr will be queried. Otherwise address_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("address_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("address_arr", inputs, opts=opts, async_method=async_method)

    def bbb(self, first: List[List[int]], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of bbb will be queried. Otherwise bbb will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("bbb", opts=opts)
        else:
            return self.simba_contract.submit_method("bbb", inputs, opts=opts, async_method=async_method)

    def nested_arr(self, first: List[List[int]], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr will be queried. Otherwise nested_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr", inputs, opts=opts, async_method=async_method)

    def nested_arr_2(self, first: List[List[int]], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr_2 will be queried. Otherwise nested_arr_2 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_2", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr_2", inputs, opts=opts, async_method=async_method)

    def nested_arr_3(self, first: List[List[int]], async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nested_arr_3 will be queried. Otherwise nested_arr_3 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nested_arr_3", opts=opts)
        else:
            return self.simba_contract.submit_method("nested_arr_3", inputs, opts=opts, async_method=async_method)

    def nested_arr_4(self, first: List[List[int]], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then nested_arr_4 will be invoked as async, otherwise nested_arr_4 will be invoked as non async
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("nested_arr_4", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("nested_arr_4", inputs, files=files, opts=opts)

    def structTest_1(self, people: List["Application.Person"], test_bool: bool, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of structTest_1 will be queried. Otherwise structTest_1 will be invoked with inputs.
        """
        inputs= {
            'people': people,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("structTest_1", opts=opts)
        else:
            return self.simba_contract.submit_method("structTest_1", inputs, opts=opts, async_method=async_method)

    def structTest_2(self, person: "Application.Person", test_bool: bool, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of structTest_2 will be queried. Otherwise structTest_2 will be invoked with inputs.
        """
        inputs= {
            'person': person,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("structTest_2", opts=opts)
        else:
            return self.simba_contract.submit_method("structTest_2", inputs, opts=opts, async_method=async_method)

    def structTest_5(self, person: "Application.Person", files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_5 will be invoked as async, otherwise structTest_5 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_5", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_5", inputs, files=files, opts=opts)

    def structTest_3(self, person: "Application.AddressPerson", files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_3 will be invoked as async, otherwise structTest_3 will be invoked as non async
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_3", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_3", inputs, files=files, opts=opts)

    def structTest_4(self, persons: List["Application.AddressPerson"], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_4 will be invoked as async, otherwise structTest_4 will be invoked as non async
        """
        inputs= {
            'persons': persons,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_4", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_4", inputs, files=files, opts=opts)

    def structTest_6(self, persons_0: List["Application.AddressPerson"], files: List[Tuple], async_method: bool = False, opts: Optional[dict] = None):
        """
        If async_method == True, then structTest_6 will be invoked as async, otherwise structTest_6 will be invoked as non async
        """
        inputs= {
            'persons_0': persons_0,
        }
        convert_classes(inputs)
        
        if async_method:
            return self.simba_contract.submit_contract_method_with_files_async("structTest_6", inputs, files=files, opts=opts)
        else:
            return self.simba_contract.submit_contract_method_with_files("structTest_6", inputs, files=files, opts=opts)

    def nowt(self, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of nowt will be queried. Otherwise nowt will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("nowt", opts=opts)
        else:
            return self.simba_contract.submit_method("nowt", inputs, opts=opts, async_method=async_method)

    def date_string(self, the_date: str, async_method: bool = False, opts: Optional[dict] = None, query_method: bool = False):
        """
        If query_method == True, then invocations of date_string will be queried. Otherwise date_string will be invoked with inputs.
        """
        inputs= {
            'the_date': the_date,
        }
        convert_classes(inputs)
        
        if query_method:
            return self.simba_contract.query_method("date_string", opts=opts)
        else:
            return self.simba_contract.submit_method("date_string", inputs, opts=opts, async_method=async_method)