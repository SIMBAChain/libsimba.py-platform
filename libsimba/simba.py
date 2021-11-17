from typing import Optional

from libsimba.simba_contract import SimbaContract
from libsimba.decorators import filter_set
from libsimba.settings import BASE_API_URL
from libsimba.simba_request import SimbaRequest

import logging
log = logging.getLogger(__name__)


class Simba:
    def __init__(self, base_api_url=BASE_API_URL):
        self.base_api_url = base_api_url  #TODO(Adam): Phase out
        SimbaRequest.base_api_url = base_api_url

    def whoami(self):
        return SimbaRequest('user/whoami/').send()

    def smart_contract_client(self, app_name, contract_name):
        return SimbaContract(self.base_api_url, app_name, contract_name)

    # -------------------------------------------------
    # All proceeding functions are general App getters
    # -------------------------------------------------
    """
    GET
    /v2/apps/
    list Application
    """
    @filter_set
    def list_applications(self, query_args: dict):
        return SimbaRequest('/v2/apps/', query_args).send()

    """
    GET
    /v2/apps/{application}/
    retrieve Application
    """
    def retrieve_application(self, app_id: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/".format(app_id), query_args).send()

    """
    GET
    /v2/apps/{application}/transactions/
    list application transactions Transaction
    """
    @filter_set
    def list_application_transactions(self, query_args: dict, app_id: str):
         return SimbaRequest("/v2/apps/{}/transactions/".format(app_id), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/
    get contract MetadataDeployedContract
    """
    def get_application_contract(self, app_id: str, contract_name: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/".format(app_id, contract_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/transactions/
    list contract transactions Transaction
    """
    @filter_set
    def list_contract_transactions(self, query_args: dict, app_id: str, contract_name: str):
        return SimbaRequest("/v2/apps/{}/contract/{}/transactions/".format(app_id, contract_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contracts/
    list contracts ExtendedDeployedContract
    """
    @filter_set
    def list_contracts(self, query_args: dict, app_id: str):
        return SimbaRequest("/v2/apps/{}/contracts/".format(app_id), query_args).send()

    """
    GET
    /v2/apps/{application}/validate/{contract_name}/{bundle_hash}/
    validate bundle BundleValidation
    """
    def validate_bundle(self, app_id: str, contract_name: str, bundle_hash: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/validate/{}/{}/".format(
            app_id, contract_name, bundle_hash), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/
    get bundle BundleData
    """
    def get_bundle(self, app_id: str, contract_name: str, bundle_hash: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/bundle/{}/".format(
            app_id, contract_name, bundle_hash), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/filename/{file_name}/
    get bundle file BundleData
    """
    def get_bundle_file(self, app_id: str, contract_name: str, bundle_hash: str, file_name, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/bundle/{}/filename/{}/".format(
            app_id, contract_name, bundle_hash, file_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/bundle/{bundle_hash}/manifest/
    list bundle manifest BundleManifest
    """
    def get_manifest_for_bundle_from_bundle_hash(self, app_id: str, contract_name: str, bundle_hash: str,
                                                 query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/bundle/{}/manifest/".format(
            app_id, contract_name, bundle_hash), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/info/
    list contract info ContractInfo
    """
    def list_contract_info(self, app_id: str, contract_name: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/info".format(app_id, contract_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/contracts/{contract_id}/
    get contract instance DeployedContractInstance
    """
    def get_instance_address(self, app_id: str, contract_name: str, contract_id: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/contracts/{}/".format(app_id, contract_name, contract_id), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/contracts/
    list contract instances DeployedContractInstance
    """
    @filter_set
    def list_contract_instances(self, query_args: dict, app_id: str, contract_name: str):
        return SimbaRequest("/v2/apps/{}/contract/{}/contracts/".format(app_id, contract_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/events/{event_name}/
    list events TransactionEvent
    """
    @filter_set
    def list_events(self, query_args: dict, app_id: str, contract_name: str, event_name: str):
        return SimbaRequest("/v2/apps/{}/contract/{}/events/{}/".format(
            app_id, contract_name, event_name), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/receipt/{hash}/
    get receipt TransactionReceipt
    """
    def get_receipt(self, app_id: str, contract_name: str, receipt_hash: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/receipt/{}/".format(
            app_id, contract_name, receipt_hash), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/transaction/{hash}/
    get transaction TransactionDetail
    """
    def get_transaction(self, app_id: str, contract_name: str, transaction_hash: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/transaction/{}/".format(
            app_id, contract_name, transaction_hash), query_args).send()

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/address/{identifier}/{method_name}/
    list instance address method ContractMethod
    """
    def call_getter_by_address(self, app_id: str, contract_name: str, identifier: str, method_name: str,
                               query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/address/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args).send()

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/address/{identifier}/{method_name}/
    post instance address method ContractMethod
    """
    def call_setter_by_address(self, app_id: str, contract_name: str, identifier: str, method_name: str, inputs: dict,
                               query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/address/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/asset/{identifier}/{method_name}/
    list instance asset method ContractMethod
    """
    def call_getter_by_asset(self, app_id: str, contract_name: str, identifier: str, method_name: str,
                             query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/asset/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args).send()

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/asset/{identifier}/{method_name}/
    post instance asset method ContractMethod
    """
    def create_instance_asset(self, app_id: str, contract_name: str, identifier: str, method_name: str, inputs: dict,
                              query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/asset/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    GET
    /v2/apps/{application}/contract/{contract_name}/{method_name}/
    list method ContractMethod
    """
    def list_contract_methods(self, app_id: str, contract_name: str, method_name: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/{}/".format(
            app_id, contract_name, method_name), query_args).send()

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/{method_name}/
    post method ContractMethod
    """
    def submit_contract_method(self, app_id: str, contract_name: str, method_name: str, inputs: dict, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/contract/{}/{}/".format(
            app_id, contract_name, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/address/{identifier}/{method_name}/
    post async instance address method ContractMethod
    """
    def call_setter_by_address_async(self, app_id: str, contract_name: str, identifier: str, method_name: str, inputs: dict,
                                     query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/async/contract/{}/address/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/asset/{identifier}/{method_name}/
    post async instance asset method ContractMethod
    """
    def create_instance_asset_async(self, app_id: str, contract_name: str, identifier: str, method_name: str, inputs: dict,
                                    query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/async/contract/{}/asset/{}/{}/".format(
            app_id, contract_name, identifier, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/async/contract/{contract_name}/{method_name}/
    post async method ContractMethod
    """
    def submit_contract_method_async(self, app_id: str, contract_name: str, method_name: str, inputs: dict,
                                     query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/async/contract/{}/{}/".format(
            app_id, contract_name, method_name), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/new/{contract_name}/
    create contract instance ContractInstance
    """
    def create_contract_instance(self, app_id: str, contract_name: str, query_args: Optional[dict] = {}):
        return SimbaRequest("/v2/apps/{}/new/{}/".format(app_id, contract_name), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/transactions/{identifier}/
    submit signed transaction SignedTransaction
    """
    #TODO(Adam): Make a transaction object to assist the user. Right now it's just a dict
    def create_contract_instance(self, app_id: str, txn_id: str, txn: dict, query_args: Optional[dict] = {}):
        return SimbaRequest(" /v2/apps/{}/transactions/{}/".format(app_id, txn_id), query_args, method="POST").send(json_payload=inputs)

    """
    POST
    /v2/apps/{application}/contract/{contract_name}/graphql/
    post gql search Application
    """
    #TODO(Adam): Add this library function for gql search
