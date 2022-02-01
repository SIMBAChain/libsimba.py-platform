from libsimba.simba import Simba
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files

class TestSimbaHinted:
    def __init__(self):
        self.app_name = "TestSimbaHinted"
        self.base_api_url = "https://api.sep.dev.simbachain.com/"
        self.contract_name = "TestSimbaHinted"
        self.simba = Simba(self.base_api_url)
        self.simba_contract = self.simba.smart_contract_client(self.app_name, self.contract_name)
    
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
    

    def nowt(self, query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of nowt will be queried. Otherwise nowt will be invoked with inputs.
        """
        inputs= {
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "nowt")
        else:
            return self.simba_contract.call_method("nowt", inputs, query_args)

    def an_arr(self, first: List[int], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of an_arr will be queried. Otherwise an_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "an_arr")
        else:
            return self.simba_contract.call_method("an_arr", inputs, query_args)

    def two_arrs(self, first: List[int], second: List[int], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of two_arrs will be queried. Otherwise two_arrs will be invoked with inputs.
        """
        inputs= {
            'first': first,
            'second': second,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "two_arrs")
        else:
            return self.simba_contract.call_method("two_arrs", inputs, query_args)

    def address_arr(self, first: List[str], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of address_arr will be queried. Otherwise address_arr will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "address_arr")
        else:
            return self.simba_contract.call_method("address_arr", inputs, query_args)

    def nested_arr_0(self, first: List[List[int]], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of nested_arr_0 will be queried. Otherwise nested_arr_0 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "nested_arr_0")
        else:
            return self.simba_contract.call_method("nested_arr_0", inputs, query_args)

    def nested_arr_1(self, first: List[List[int]], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of nested_arr_1 will be queried. Otherwise nested_arr_1 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "nested_arr_1")
        else:
            return self.simba_contract.call_method("nested_arr_1", inputs, query_args)

    def nested_arr_2(self, first: List[List[int]], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of nested_arr_2 will be queried. Otherwise nested_arr_2 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "nested_arr_2")
        else:
            return self.simba_contract.call_method("nested_arr_2", inputs, query_args)

    def nested_arr_3(self, first: List[List[int]], query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of nested_arr_3 will be queried. Otherwise nested_arr_3 will be invoked with inputs.
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "nested_arr_3")
        else:
            return self.simba_contract.call_method("nested_arr_3", inputs, query_args)

    def nested_arr_4(self, first: List[List[int]], files: List[Tuple], query_args: Optional[dict] = None):
        """
        If async_method == True, then nested_arr_4 will be invoked as async, otherwise nested_arr_4 will be invoked as non async
        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object).
            see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs= {
            'first': first,
        }
        convert_classes(inputs)
        files = open_files(files)
        response = self.simba_contract.call_contract_method_with_files("nested_arr_4", inputs, files, query_args)
        close_files(files)
        return response

    def structTest_1(self, people: List["TestSimbaHinted.Person"], test_bool: bool, query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of structTest_1 will be queried. Otherwise structTest_1 will be invoked with inputs.
        """
        inputs= {
            'people': people,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "structTest_1")
        else:
            return self.simba_contract.call_method("structTest_1", inputs, query_args)

    def structTest_2(self, person: "TestSimbaHinted.Person", test_bool: bool, query_args: Optional[dict] = None, qry_mth: Optional[bool] = False):
        """
        If qry_mth == True, then invocations of structTest_2 will be queried. Otherwise structTest_2 will be invoked with inputs.
        """
        inputs= {
            'person': person,
            'test_bool': test_bool,
        }
        convert_classes(inputs)
        if qry_mth:
            return self.simba_contract.query_method(query_args, "structTest_2")
        else:
            return self.simba_contract.call_method("structTest_2", inputs, query_args)

    def structTest_3(self, person: "TestSimbaHinted.AddressPerson", files: List[Tuple], query_args: Optional[dict] = None):
        """
        If async_method == True, then structTest_3 will be invoked as async, otherwise structTest_3 will be invoked as non async
        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object).
            see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        files = open_files(files)
        response = self.simba_contract.call_contract_method_with_files("structTest_3", inputs, files, query_args)
        close_files(files)
        return response

    def structTest_4(self, persons: List["TestSimbaHinted.AddressPerson"], files: List[Tuple], query_args: Optional[dict] = None):
        """
        If async_method == True, then structTest_4 will be invoked as async, otherwise structTest_4 will be invoked as non async
        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object).
            see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs= {
            'persons': persons,
        }
        convert_classes(inputs)
        files = open_files(files)
        response = self.simba_contract.call_contract_method_with_files("structTest_4", inputs, files, query_args)
        close_files(files)
        return response

    def structTest_5(self, person: "TestSimbaHinted.Person", files: List[Tuple], query_args: Optional[dict] = None):
        """
        If async_method == True, then structTest_5 will be invoked as async, otherwise structTest_5 will be invoked as non async
        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object).
            see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs= {
            'person': person,
        }
        convert_classes(inputs)
        files = open_files(files)
        response = self.simba_contract.call_contract_method_with_files("structTest_5", inputs, files, query_args)
        close_files(files)
        return response
