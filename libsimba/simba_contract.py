import requests
import json
from libsimba.decorators import auth_required
from libsimba.utils import build_url

class SimbaContract:
    def __init__(self, base_api_url, app_name, contract_name):
        self.app_name = app_name
        self.contract_name = contract_name
        self.base_api_url = base_api_url
        self.contract_uri = "{}/contract/{}".format(self.app_name, self.contract_name)

    @auth_required
    def query_method(self, headers, method_name, opts={}):
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(self.contract_uri, method_name), opts)
        return requests.get(url, headers=headers)
    
    @auth_required
    def submit_method(self, headers, method_name, inputs, opts={}):
        url = build_url(self.base_api_url, "v2/apps/{}/{}/".format(self.contract_uri, method_name), opts)
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        return requests.post(url, headers=headers, data=payload)

    @auth_required
    def submit_contract_method_with_files(self, headers, method_name, inputs, file, opts={}):
        # TODO(Adam): figure out files
        pass

    @auth_required
    def get_transactions(self, headers, opts={}):
        url = build_url(self.base_api_url, "v2/apps/{}/transactions/".format(self.contract_uri), opts)
        return requests.get(url, headers=headers)

    @auth_required
    def validate_bundle_hash(self, headers, bundle_hash, opts={}):
        url = build_url(self.base_api_url, "v2/apps/{}/validate/{}/{}".format(self.app_name, self.contract_name, bundle_hash), opts)
        return requests.get(url, headers=headers)