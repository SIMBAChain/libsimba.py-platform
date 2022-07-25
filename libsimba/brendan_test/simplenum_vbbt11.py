from libsimba.simba import Simba
from libsimba.simba_sync import SimbaSync
from libsimba.settings import BASE_API_URL
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from libsimba.utils import SearchFilter

class Simplenum_vbbt11:
    def __init__(self):
        self.app_name = "BrendanTestApp"
        self.base_api_url = BASE_API_URL
        self.contract_name = "simplenum_vbbt11"
        self.simba = Simba(self.base_api_url)
        self.simba_sync = SimbaSync(self.base_api_url)
        self.simba_contract = self.simba.smart_contract_client(self.app_name, self.contract_name)
        self.simba_contract_sync = self.simba_sync.smart_contract_client(self.app_name, self.contract_name)

    
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
    