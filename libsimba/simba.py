import requests
from libsimba.auth import Auth
from libsimba.decorators import auth_required
from libsimba.utils import build_url
from libsimba.settings import BASE_API_URL, DEBUG

class Simba:
    def __init__(self):
        # self.organization = organization
        self.v2_apps_uri = build_url(BASE_API_URL, "/v2/apps/", {})

    # TEST method
    @staticmethod
    def main():
        simba = Simba()
        user_info = simba.whoami()
        print(user_info)
        apps = simba.list_application()
        print(apps)

    @auth_required
    def whoami(self, headers):
        whoami_url = build_url(BASE_API_URL, "user/whoami/", {})
        r = requests.get(whoami_url, headers=headers)
        return r.json()

    """
    GET
    ​/v2​/apps​/
    list Application
    """
    @auth_required
    def list_application(self, headers):
        r = requests.get(self.v2_apps_uri, headers=headers)
        return r.json()

    """
    GET
    ​/v2​/apps​/{application}​/
    retrieve Application
    GET
    ​/v2​/apps​/{application}​/redoc​/
    list app redoc Application
    GET
    ​/v2​/apps​/{application}​/yaml​/
    list app swagger Application
    GET
    ​/v2​/apps​/{application}​/openapi_v2​/
    list app swagger v2 Application
    GET
    ​/v2​/apps​/{application}​/transactions​/
    list application transactions Transaction
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/
    get contract MetadataDeployedContract
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/{method_name}​/csv​/
    list contract method transaction csv Csv
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/csv​/
    list contract transaction csv Csv
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/transactions​/
    list contract transactions Transaction
    GET
    ​/v2​/apps​/{application}​/contracts​/
    list contracts ExtendedDeployedContract
    GET
    ​/v2​/apps​/{application}​/validate​/{contract_name}​/{bundle_hash}​/
    validate bundle BundleValidation
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/bundle​/{bundle_hash}​/
    get bundle BundleData
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/bundle​/{bundle_hash}​/filename​/{file_name}​/
    get bundle file BundleData
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/bundle​/{bundle_hash}​/manifest​/
    list bundle manifest BundleManifest
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/info​/
    list contract info ContractInfo
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/contracts​/{contract_id}​/
    get contract instance DeployedContractInstance
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/contracts​/
    list contract instances DeployedContractInstance
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/events​/{event_name}​/
    list events TransactionEvent
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/receipt​/{hash}​/
    get receipt TransactionReceipt
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/transaction​/{hash}​/
    get transaction TransactionDetail
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/address​/{identifier}​/{method_name}​/
    list instance address method ContractMethod
    POST
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/address​/{identifier}​/{method_name}​/
    post instance address method ContractMethod
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/asset​/{identifier}​/{method_name}​/
    list instance asset method ContractMethod
    POST
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/asset​/{identifier}​/{method_name}​/
    post instance asset method ContractMethod
    GET
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/{method_name}​/
    list method ContractMethod
    POST
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/{method_name}​/
    post method ContractMethod
    POST
    ​/v2​/apps​/{application}​/async​/contract​/{contract_name}​/address​/{identifier}​/{method_name}​/
    post async instance address method ContractMethod
    POST
    ​/v2​/apps​/{application}​/async​/contract​/{contract_name}​/asset​/{identifier}​/{method_name}​/
    post async instance asset method ContractMethod
    POST
    ​/v2​/apps​/{application}​/async​/contract​/{contract_name}​/{method_name}​/
    post async method ContractMethod
    POST
    ​/v2​/apps​/{application}​/new​/{contract_name}​/
    create contract instance ContractInstance
    POST
    ​/v2​/apps​/{application}​/transactions​/{identifier}​/
    submit signed transaction SignedTransaction
    POST
    ​/v2​/apps​/{application}​/contract​/{contract_name}​/graphql​/
    post gql search Application
    """

if DEBUG is True and __name__ == "__main__":
    Simba.main()
