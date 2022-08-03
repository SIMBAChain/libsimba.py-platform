from libsimba.simba import Simba
from libsimba.simba_sync import SimbaSync
from libsimba.settings import BASE_API_URL
from typing import List, Tuple, Dict, Any, Optional
from libsimba.class_converter import ClassToDictConverter, convert_classes
from libsimba.file_handler import open_files, close_files
from libsimba.utils import SearchFilter

class {{SimbaHintedContractObj.contract_class_name}}:
    def __init__(self):
        self.app_name = "{{SimbaHintedContractObj.app_name}}"
        self.base_api_url = BASE_API_URL
        self.contract_name = "{{SimbaHintedContractObj.contract_name}}"
        self.simba = Simba(self.base_api_url)
        self.simba_sync = SimbaSync(self.base_api_url)
        self.simba_contract = self.simba.smart_contract_client(self.app_name, self.contract_name)
        self.simba_contract_sync = self.simba_sync.smart_contract_client(self.app_name, self.contract_name)

    {% for cls in SimbaHintedContractObj.classes_from_structs() -%}
    class {{ cls["class_name"] }}(ClassToDictConverter):
        def __init__(
            self,
            {%- for component in cls["components"] -%}
            {%- if loop.last %}
            {{component["comp_name"]}}: {{component["comp_type"]}} = {{ component["default_value"]}}):
            {%- else %}
            {{component["comp_name"]}}: {{component["comp_type"]}} = {{ component["default_value"]}},
            {%- endif %}
            {%- endfor %}
            {% for component in cls["components"] -%}
            self.{{ component["comp_name"]}} = {{ component["comp_name"]}}
            {% endfor %}
    {% endfor -%}
    {%- for method_dict in SimbaHintedContractObj.info_for_all_methods() %}
    {%- set accepts_files = method_dict["accepts_files"] %}
    {%- set is_accessor = method_dict["is_accessor"] %}
    {%- set method_name = method_dict["method_name"] %}
    async def {{method_name}}(
        self,
        {% if method_dict["param_info"] -%}
        {% for input_dict in method_dict["param_info"] -%}
        {%- set param_name = input_dict["param_name"] -%}
        {%- set hint_type = input_dict["hint_type"] -%}
        {%- set default_value = input_dict["default_value"] -%}
        {{param_name}}: {{hint_type}} = {{default_value}},
        {% endfor -%}
        {%- endif -%}
        {% if accepts_files -%}
        files: List[Tuple] = None,
        {% endif -%}
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        {%- if accepts_files %}
        """
        If do_query == True, then invocations of {{method_name}} will be queried. Otherwise {{method_name}} will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        {%- else %}
        """
        If do_query == True, then invocations of {{method_name}} will be queried. Otherwise {{method_name}} will be invoked with inputs.
        """
        {%- endif %}
        inputs = {
            {%- for input_dict in method_dict["param_info"] %}
            {%- set param_name = input_dict["param_name"] %}
            {%- set original_param_name = input_dict["original_param_name"] %}
            "{{original_param_name}}": {{param_name}},
            {%- endfor %}
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = await self.simba_contract.query_method("{{method_name}}", query_args = query_args, search_filter = search_filter)
            return res
        else:
            {% if accepts_files -%}
            files = open_files(files)
            res = await self.simba_contract.call_contract_method_with_files("{{method_name}}", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
            {%- else -%}
            {% if is_accessor -%}
            res = await self.simba_contract.call_method("{{method_name}}", inputs, query_args = query_args)
            return res
            {%- else -%}
            res = await self.simba_contract.submit_method("{{method_name}}", inputs, query_args = query_args)
            return res
            {%- endif -%}
            {%- endif %}

    def {{method_name}}_sync(
        self,
        {% if method_dict["param_info"] -%}
        {% for input_dict in method_dict["param_info"] -%}
        {%- set param_name = input_dict["param_name"] -%}
        {%- set hint_type = input_dict["hint_type"] -%}
        {%- set default_value = input_dict["default_value"] -%}
        {{param_name}}: {{hint_type}} = {{default_value}},
        {% endfor -%}
        {%- endif -%}
        {% if accepts_files -%}
        files: List[Tuple] = None,
        {% endif -%}
        query_args: Optional[dict] = None,
        do_query: Optional[bool] = False,
        search_filter: SearchFilter = None):
        {%- if accepts_files %}
        """
        If do_query == True, then invocations of {{method_name}} will be queried. Otherwise {{method_name}} will be invoked with inputs.

        files parameter should be list with tuple elements of form (file_name, file_path) or (file_name, readable_file_like_object). see libsimba.file_handler for further details on what open_files expects as arguments
        """
        {%- else %}
        """
        If do_query == True, then invocations of {{method_name}} will be queried. Otherwise {{method_name}} will be invoked with inputs.
        
        """
        {%- endif %}
        inputs = {
            {%- for input_dict in method_dict["param_info"] %}
            {%- set param_name = input_dict["param_name"] %}
            {%- set original_param_name = input_dict["original_param_name"] %}
            "{{original_param_name}}": {{param_name}},
            {%- endfor %}
        }
        convert_classes(inputs)
        query_args = query_args or {}
        if do_query:
            res = self.simba_contract_sync.query_method("{{method_name}}", query_args = query_args, search_filter = search_filter)
            return res
        else:
            {% if accepts_files -%}
            files = open_files(files)
            res = self.simba_contract_sync.call_contract_method_with_files("{{method_name}}", inputs, files = files, query_args = query_args)
            close_files(files)
            return res
            {%- else -%}
            {% if is_accessor -%}
            res = self.simba_contract_sync.call_method("{{method_name}}", inputs, query_args = query_args)
            return res
            {%- else -%}
            res = self.simba_contract_sync.submit_method("{{method_name}}", inputs, query_args = query_args)
            return res
            {%- endif -%}
            {%- endif %}
    {% endfor %}