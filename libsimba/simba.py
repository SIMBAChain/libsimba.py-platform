import json
import os
from typing import Optional

import requests
# DEBUG SETTINGS
from libsimba.settings import DEBUG, TEST_APP, TEST_CONTRACT, TEST_METHOD, TEST_INPUTS

from libsimba.simba_contract import SimbaContract
from libsimba.decorators import auth_required
from libsimba.utils import build_url
from libsimba.settings import BASE_API_URL

import logging
log = logging.getLogger(__name__)


class Simba:
    def __init__(self, base_api_url=BASE_API_URL):
        self.base_api_url = base_api_url

    @auth_required
    def whoami(self, headers):
        whoami_url = build_url(BASE_API_URL, "user/whoami/", {})
        return requests.get(whoami_url, headers=headers)

    def get_contract(self, app_name, contract_name):
        return SimbaContract(self.base_api_url, app_name, contract_name)

    # -------------------------------------------------
    # All proceeding functions are general App getters
    # -------------------------------------------------
    """
    GET
    /v2/apps/
    list Application
    """
    @auth_required
    def list_applications(self, headers):
        r = requests.get(self.base_api_url, headers=headers)
        return r.json()['results']

    """
    GET
    /v2/apps/{application}/
    retrieve Application
    """
    @auth_required
    def retrieve_application(self, headers, app_id, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/".format(app_id), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/transactions/
    list application transactions Transaction
    """
    @auth_required
    def list_application_transactions(self, headers, app_id, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/transactions/".format(app_id), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/
    get contract MetadataDeployedContract
    """
    @auth_required
    def get_application_contract(self, headers, app_id, contract_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/".format(app_id, contract_name), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/transactions/
    list contract transactions Transaction
    """
    @auth_required
    def list_contract_transactions(self, headers, app_id, contract_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/transactions/".format(app_id, contract_name), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contracts/
    list contracts ExtendedDeployedContract
    """
    @auth_required
    def list_contracts(self, headers, app_id, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contracts/".format(app_id), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/validate/{contract_name}/{bundle_hash}/
    validate bundle BundleValidation
    """
    @auth_required
    def validate_bundle(self, headers, app_id, contract_name, bundle_hash, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/validate/{}/{}/".format(
            app_id, contract_name, bundle_hash), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/
    get bundle BundleData
    """
    @auth_required
    def get_bundle(self, headers, app_id, contract_name, bundle_hash, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/bundle/{}/".format(
            app_id, contract_name, bundle_hash), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/filename/{file_name}/
    get bundle file BundleData
    """
    @auth_required
    def get_bundle_file(self, headers, app_id, contract_name, bundle_hash, file_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/bundle/{}/filename/{}/".format(
            app_id, contract_name, bundle_hash, file_name), opts)
        return requests.get(url, headers=headers)


    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/manifest/
    list bundle manifest BundleManifest
    """
    @auth_required
    def get_manifest_for_bundle_from_bundle_hash(self, headers, app_id, contract_name, bundle_hash,
                                                 opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/bundle/{}/manifest/".format(
            app_id, contract_name, bundle_hash), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/info/
    list contract info ContractInfo
    """
    @auth_required
    def list_contract_info(self, headers, app_id, contract_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/info".format(app_id, contract_name), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/contracts/{contract_id}/
    get contract instance DeployedContractInstance
    """
    @auth_required
    def get_instance_address(self, headers, app_id, contract_name, contract_id, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/contracts/{}/".format(app_id, contract_name, contract_id), opts)
        r = requests.get(url, headers=headers)
        return r.json()['address']

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/contracts/
    list contract instances DeployedContractInstance
    """
    @auth_required
    def list_contract_instances(self, headers, app_id, contract_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/contracts/".format(app_id, contract_name), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/events/{event_name}/
    list events TransactionEvent
    """
    @auth_required
    def list_events(self, headers, app_id, contract_name, event_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/events/{}/".format(
            app_id, contract_name, event_name), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/receipt/{hash}/
    get receipt TransactionReceipt
    """
    @auth_required
    def get_receipt(self, headers, app_id, contract_name, receipt_hash, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/receipt/{}/".format(
            app_id, contract_name, receipt_hash), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/transaction/{hash}/
    get transaction TransactionDetail
    """
    @auth_required
    def get_transaction(self, headers, app_id, contract_name, transaction_hash, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/transaction/{}/".format(
            app_id, contract_name, transaction_hash), opts)
        return requests.get(url, headers=headers)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/address/{identifier}/{method_name}/
    list instance address method ContractMethod
    """
    @auth_required
    def call_getter_by_address(self, headers, app_id, contract_name, identifier, method_name,
                               opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/address/{}/{}/".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.get(url, headers=headers)

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/address/{identifier}/{method_name}/
    post instance address method ContractMethod
    """
    @auth_required
    def call_setter_by_address(self, headers, app_id, contract_name, identifier, method_name, inputs,
                               opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/address/{}/{}/".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/asset/{identifier}/{method_name}/
    list instance asset method ContractMethod
    """
    @auth_required
    def call_getter_by_asset(self, headers, app_id, contract_name, identifier, method_name,
                             opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/asset/{}/{}/".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.get(url, headers=headers)

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/asset/{identifier}/{method_name}/
    post instance asset method ContractMethod
    """
    @auth_required
    def create_instance_asset(self, headers, app_id, contract_name, identifier, method_name, inputs,
                              opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/asset/{}/{}".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/{method_name}/
    list method ContractMethod
    """
    @auth_required
    def list_contract_methods(self, headers, app_id, contract_name, method_name, opts: Optional[dict] = None):
        opts = opts or {}
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/{}/".format(
            app_id, contract_name, method_name), opts)
        return requests.get(url, headers=headers)

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/{method_name}/
    post method ContractMethod
    """
    @auth_required
    def submit_contract_method(self, headers, app_id, contract_name, method_name, inputs, opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/contract/{}/{}".format(
            app_id, contract_name, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/address/{identifier}/{method_name}/
    post async instance address method ContractMethod
    """
    @auth_required
    def call_setter_by_address_async(self, headers, app_id, contract_name, identifier, method_name, inputs,
                                     opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/async/contract/{}/address/{}/{}".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/asset/{identifier}/{method_name}/
    post async instance asset method ContractMethod
    """
    @auth_required
    def create_instance_asset_async(self, headers, app_id, contract_name, identifier, method_name, inputs,
                                    opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/async/contract/{}/asset/{}/{}".format(
            app_id, contract_name, identifier, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/{method_name}/
    post async method ContractMethod
    """
    @auth_required
    def submit_contract_method_async(self, headers, app_id, contract_name, method_name, inputs,
                                     opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/async/contract/{}/{}".format(
            app_id, contract_name, method_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/new/{contract_name}/
    create contract instance ContractInstance
    """
    @auth_required
    def create_contract_instance(self, headers, app_id, contract_name, opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps(inputs)
        url = build_url(self.base_api_url, "/v2/apps/{}/new/{}/".format(app_id, contract_name), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/transactions/{identifier}/
    submit signed transaction SignedTransaction
    """
    @auth_required
    def create_contract_instance(self, headers, app_id, txn_id, txn, opts: Optional[dict] = None):
        opts = opts or {}
        headers['content-type'] = 'application/json'
        payload = json.dumps({'transaction': txn})
        url = build_url(self.base_api_url, " /v2/apps/{}/transactions/{}/".format(app_id, txn_id), opts)
        return requests.post(url, headers=headers, data=payload)

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/graphql/
    post gql search Application
    """

    # ----------------------------------------------
    # Test methods
    # ----------------------------------------------
    @staticmethod
    def test():
        logging.basicConfig(level=os.environ.get("SIMBA_LOGLEVEL", "DEBUG"))

        if DEBUG is False:
            log.info('Debug is False, not running tests')
            return

        simba = Simba(BASE_API_URL)
        contract = simba.get_contract(TEST_APP, TEST_CONTRACT)
        log.info('{} :: {} :: {}'.format(BASE_API_URL, TEST_APP, TEST_CONTRACT))

        r = contract.submit_method(TEST_METHOD, TEST_INPUTS)
        log.info(r.text)
        assert (r.status_code >= 200 and r.status_code <= 299)
        log.info(r.json())

        r = contract.query_method(TEST_METHOD)
        assert (r.status_code >= 200 and r.status_code <= 299)
        log.info(r.json())


if DEBUG is True and __name__ == '__main__':
    Simba.test()
