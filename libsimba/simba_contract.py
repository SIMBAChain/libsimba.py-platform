from typing import List, Optional, Any, Dict

import requests
import json
from libsimba.decorators import auth_required
from libsimba.utils import build_url
from libsimba.param_checking_contract import ParamCheckingContract


class SimbaContract(ParamCheckingContract):
    def __init__(self, base_api_url, app_name, contract_name):
        self.app_name = app_name
        self.contract_name = contract_name
        self.base_api_url = base_api_url
        self.contract_uri = "{}/contract/{}".format(self.app_name, self.contract_name)
        self.async_contract_uri = "{}/async/contract/{}".format(self.app_name, self.contract_name)
        self.metadata = self.get_metatadata()
        self.params_restricted = self.param_restrictions()

    @auth_required 
    def get_metadata(self, headers):
        url = build_url(self.base_api_url, "v2/apps/{}/contract/{}/?format=json".format(self.contract_name, self.app_name)) 
        return requests.get(url, headers=headers)

    @auth_required
    def query_method(self, headers, method_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(self.contract_uri, method_name), opts)
        return requests.get(url, headers=headers)
    
    @auth_required
    def submit_method(self, headers, method_name, inputs, opts: Optional[dict] = None, async_method=False):
        self.validate_params(method_name, inputs)
        opts = opts or {}
        contract_uri = self.contract_uri if async_method is False else self.async_contract_uri
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(contract_uri, method_name), opts)
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        return requests.post(url, headers=headers, data=payload)

    @auth_required
    def submit_method_async(self, headers, method_name, inputs, opts: Optional[dict] = None):
        self.validate_params(method_name, inputs)
        return self.submit_method(headers, method_name, inputs, opts, async_method=True)

    @auth_required
    def submit_contract_method_with_files(self, headers, method_name, inputs, files=None, opts: Optional[dict] = None):
        self.validate_params(method_name, inputs)
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(self.contract_uri, method_name), opts)
        if files:
            return requests.post(url, headers=headers, data=inputs, files=files)
        else:
            return requests.post(url, headers=headers, data=inputs)

    @auth_required
    def submit_contract_method_with_files_async(self, headers, method_name, inputs, files=None,
                                                opts: Optional[dict] = None):
        self.validate_params(method_name, inputs)
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(self.async_contract_uri, method_name), opts)
        payload = json.dumps(inputs)
        if files:
            return requests.post(url, headers=headers, data=payload, files=files)
        else:
            return requests.post(url, headers=headers, data=payload)

    @auth_required
    def get_transactions(self, headers, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/transactions/".format(self.contract_uri), opts)
        return requests.get(url, headers=headers)

    @auth_required
    def validate_bundle_hash(self, headers, bundle_hash, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "v2/apps/{}/validate/{}/{}".format(self.app_name, self.contract_name, bundle_hash), opts)
        return requests.get(url, headers=headers)

    @auth_required
    def get_transaction_statuses(self, headers, txn_hashes: List[str] = None, opts: Optional[dict] = None):
        # transaction status for a list of txn hashes
        # filter[transaction_hash.in] can be a key in opts, or the txn_hashes param
        # if filter is not in the opts, and txn_hashes is given,
        # this method correctly formats the filter string in opts
        opts = opts or {}
        if isinstance(txn_hashes, str):
            txn_hashes = [txn_hashes]
        if 'filter[transaction_hash.in]' not in opts and txn_hashes:
            opts['filter[transaction_hash.in]'] = ','.join(txn_hashes)
        url = build_url(self.base_api_url, "v2/apps/{}/contract/{}/transactions".format(
            self.app_name, self.contract_name
        ), opts)
        return requests.get(url, headers=headers)

#%%
