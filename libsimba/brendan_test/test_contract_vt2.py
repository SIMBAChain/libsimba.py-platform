from libsimba.simba import Simba
from libsimba.simba_sync import SimbaSync
from libsimba.settings import BASE_API_URL
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from libsimba.utils import SearchFilter

class Test_contract_vt2:
    def __init__(self):
        self.app_name = "BrendanTestApp"
        self.base_api_url = BASE_API_URL
        self.contract_name = "test_contract_vt2"
        self.simba = Simba(self.base_api_url)
        self.simba_sync = SimbaSync(self.base_api_url)
        self.simba_contract = self.simba.smart_contract_client(self.app_name, self.contract_name)
        self.simba_contract_sync = self.simba_sync.smart_contract_client(self.app_name, self.contract_name)

    class Addr(ClassToDictConverter):
        def __init__(
            self,
            street: str = "None",
            number: int = None,
            town: str = "None"):
            self.street = street
            self.number = number
            self.town = town
            
    class Person(ClassToDictConverter):
        def __init__(
            self,
            name: str = "None",
            age: int = None,
            addr: "Test_contract_vt2.Addr" = None):
            self.name = name
            self.age = age
            self.addr = addr
            
    class AddressPerson(ClassToDictConverter):
        def __init__(
            self,
            name: str = "None",
            age: int = None,
            addrs: List["Test_contract_vt2.Addr"] = None):
            self.name = name
            self.age = age
            self.addrs = addrs
            
    
    async def nowT(
        self,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nowT will be queried. Otherwise nowT will be invoked with inputs.
        """
        inputs = {
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nowT", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("nowT", inputs, query_args = query_args)
            return res

    def nowT_sync(
        self,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nowT will be queried. Otherwise nowT will be invoked with inputs.
        
        """
        inputs = {
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nowT", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("nowT", inputs, query_args = query_args)
            return res
    
    async def anArr(
        self,
        first: List[int] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of anArr will be queried. Otherwise anArr will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("anArr", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("anArr", inputs, query_args = query_args)
            return res

    def anArr_sync(
        self,
        first: List[int] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of anArr will be queried. Otherwise anArr will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("anArr", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("anArr", inputs, query_args = query_args)
            return res
    
    async def getNum(
        self,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of getNum will be queried. Otherwise getNum will be invoked with inputs.
        """
        inputs = {
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("getNum", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.call_method("getNum", inputs, query_args = query_args)
            return res

    def getNum_sync(
        self,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of getNum will be queried. Otherwise getNum will be invoked with inputs.
        
        """
        inputs = {
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("getNum", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.call_method("getNum", inputs, query_args = query_args)
            return res
    
    async def setNum(
        self,
        _ourNum: int = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of setNum will be queried. Otherwise setNum will be invoked with inputs.
        """
        inputs = {
            "_ourNum": _ourNum,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("setNum", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("setNum", inputs, query_args = query_args)
            return res

    def setNum_sync(
        self,
        _ourNum: int = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of setNum will be queried. Otherwise setNum will be invoked with inputs.
        
        """
        inputs = {
            "_ourNum": _ourNum,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("setNum", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("setNum", inputs, query_args = query_args)
            return res
    
    async def twoArrs(
        self,
        first: List[int] = None,
        second: List[int] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of twoArrs will be queried. Otherwise twoArrs will be invoked with inputs.
        """
        inputs = {
            "first": first,
            "second": second,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("twoArrs", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("twoArrs", inputs, query_args = query_args)
            return res

    def twoArrs_sync(
        self,
        first: List[int] = None,
        second: List[int] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of twoArrs will be queried. Otherwise twoArrs will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
            "second": second,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("twoArrs", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("twoArrs", inputs, query_args = query_args)
            return res
    
    async def addressArr(
        self,
        first: List[str] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of addressArr will be queried. Otherwise addressArr will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("addressArr", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("addressArr", inputs, query_args = query_args)
            return res

    def addressArr_sync(
        self,
        first: List[str] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of addressArr will be queried. Otherwise addressArr will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("addressArr", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("addressArr", inputs, query_args = query_args)
            return res
    
    async def nestedArr0(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr0 will be queried. Otherwise nestedArr0 will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nestedArr0", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("nestedArr0", inputs, query_args = query_args)
            return res

    def nestedArr0_sync(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr0 will be queried. Otherwise nestedArr0 will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nestedArr0", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("nestedArr0", inputs, query_args = query_args)
            return res
    
    async def nestedArr1(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr1 will be queried. Otherwise nestedArr1 will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nestedArr1", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("nestedArr1", inputs, query_args = query_args)
            return res

    def nestedArr1_sync(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr1 will be queried. Otherwise nestedArr1 will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nestedArr1", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("nestedArr1", inputs, query_args = query_args)
            return res
    
    async def nestedArr2(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr2 will be queried. Otherwise nestedArr2 will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nestedArr2", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("nestedArr2", inputs, query_args = query_args)
            return res

    def nestedArr2_sync(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr2 will be queried. Otherwise nestedArr2 will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nestedArr2", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("nestedArr2", inputs, query_args = query_args)
            return res
    
    async def nestedArr3(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr3 will be queried. Otherwise nestedArr3 will be invoked with inputs.
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nestedArr3", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("nestedArr3", inputs, query_args = query_args)
            return res

    def nestedArr3_sync(
        self,
        first: List[List[int]] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr3 will be queried. Otherwise nestedArr3 will be invoked with inputs.
        
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nestedArr3", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("nestedArr3", inputs, query_args = query_args)
            return res
    
    async def nestedArr4(
        self,
        first: List[List[int]] = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr4 will be queried. Otherwise nestedArr4 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("nestedArr4", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("nestedArr4", inputs, files = files, query_args = query_args)
            close_files(files)
            return res

    def nestedArr4_sync(
        self,
        first: List[List[int]] = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of nestedArr4 will be queried. Otherwise nestedArr4 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "first": first,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("nestedArr4", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("nestedArr4", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
    
    async def structTest1(
        self,
        people: List["Test_contract_vt2.Person"] = None,
        test_bool: bool = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest1 will be queried. Otherwise structTest1 will be invoked with inputs.
        """
        inputs = {
            "people": people,
            "test_bool": test_bool,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("structTest1", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("structTest1", inputs, query_args = query_args)
            return res

    def structTest1_sync(
        self,
        people: List["Test_contract_vt2.Person"] = None,
        test_bool: bool = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest1 will be queried. Otherwise structTest1 will be invoked with inputs.
        
        """
        inputs = {
            "people": people,
            "test_bool": test_bool,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("structTest1", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("structTest1", inputs, query_args = query_args)
            return res
    
    async def structTest2(
        self,
        person: "Test_contract_vt2.Person" = None,
        test_bool: bool = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest2 will be queried. Otherwise structTest2 will be invoked with inputs.
        """
        inputs = {
            "person": person,
            "test_bool": test_bool,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("structTest2", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = await self.simba_contract.submit_method("structTest2", inputs, query_args = query_args)
            return res

    def structTest2_sync(
        self,
        person: "Test_contract_vt2.Person" = None,
        test_bool: bool = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest2 will be queried. Otherwise structTest2 will be invoked with inputs.
        
        """
        inputs = {
            "person": person,
            "test_bool": test_bool,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("structTest2", query_args = query_args, search_filter = search_filter)
            return res
        else:
            res = self.simba_contract_sync.submit_method("structTest2", inputs, query_args = query_args)
            return res
    
    async def structTest3(
        self,
        person: "Test_contract_vt2.AddressPerson" = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest3 will be queried. Otherwise structTest3 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("structTest3", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("structTest3", inputs, files = files, query_args = query_args)
            close_files(files)
            return res

    def structTest3_sync(
        self,
        person: "Test_contract_vt2.AddressPerson" = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest3 will be queried. Otherwise structTest3 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("structTest3", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("structTest3", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
    
    async def structTest4(
        self,
        persons: List["Test_contract_vt2.AddressPerson"] = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest4 will be queried. Otherwise structTest4 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "persons": persons,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("structTest4", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("structTest4", inputs, files = files, query_args = query_args)
            close_files(files)
            return res

    def structTest4_sync(
        self,
        persons: List["Test_contract_vt2.AddressPerson"] = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest4 will be queried. Otherwise structTest4 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "persons": persons,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("structTest4", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("structTest4", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
    
    async def structTest5(
        self,
        person: "Test_contract_vt2.Person" = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest5 will be queried. Otherwise structTest5 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("structTest5", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("structTest5", inputs, files = files, query_args = query_args)
            close_files(files)
            return res

    def structTest5_sync(
        self,
        person: "Test_contract_vt2.Person" = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of structTest5 will be queried. Otherwise structTest5 will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("structTest5", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("structTest5", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
    
    async def clientContainer(
        self,
        person: "Test_contract_vt2.Person" = None,
        _bundlePath: str = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of clientContainer will be queried. Otherwise clientContainer will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
            "_bundlePath": _bundlePath,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("clientContainer", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("clientContainer", inputs, files = files, query_args = query_args)
            close_files(files)
            return res

    def clientContainer_sync(
        self,
        person: "Test_contract_vt2.Person" = None,
        _bundlePath: str = None,
        files: List[Tuple] = None,
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        """
        If do_query == True, then invocations of clientContainer will be queried. Otherwise clientContainer will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        inputs = {
            "person": person,
            "_bundlePath": _bundlePath,
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("clientContainer", query_args = query_args, search_filter = search_filter)
            return res
        else:
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("clientContainer", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
    