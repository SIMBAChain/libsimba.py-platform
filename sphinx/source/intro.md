# LibSimba.py
## *Installation*

Requires Python >= 3.7

```
pip install libsimba.py-platform
```

### *Install from package:*
View our [releases](https://github.com/SIMBAChain/libsimba.py-platform/releases/) and download the tarball for the chosen release.
```
pip install libsimba.py-platform-0.1.4.tar.gz
```

### *Install for development*

```
git clone https://github.com/SIMBAChain/libsimba.py-platform.git
cd libsimba.py-platform
poetry env use python3.7
poetry install
```
Alternatively, using virtualenv:

```
git clone https://github.com/SIMBAChain/libsimba.py-platform.git
libsimba.py-platform
virtualenv -p python3 .venv
source .venv/bin/activate
poetry install
```

## *Configuration*

### Django OAuth2 Toolkit Authentication
Most users' environments will be using Django OAuth2 Toolkit for authentication. YOu will need to set some configuration variables to use this authentication flow (see below). To set these variables, you can either set environment variables, or you can create a .env file in the root of your project (in your libsimba.py-platform directory). 

If you're using a .env file, then an example file would look like (the SECRET and ID in this example are fake):

```
BASE_API_URL="https://simba-dev-api.platform.simbachain.com/"
AUTH_FLOW="client_credentials"
CLIENT_SECRET="ASwe29JUHhhIHsih238hfs8w7HSD88hah823hsdhHWE8665sdhfhjsdjHUSHHh92387hahHHS239823AJHhsdjcbjs09283jsd98JHHhw192301Hyihsn91ncmzhjkaO"
CLIENT_ID="oiquwyeOIHbwe78ashah928H80jh2190hbWYHBnl"
BASE_AUTH_URL="https://simba-dev-api.platform.simbachain.com"
AUTH_ENDPOINT="/o/"
```

Note on the above variables from your .env file:
1. AUTH_FLOW defaults to "client credentials" if not set
2. BASE_AUTH_URL defaults to "https://simba-dev-api.platform.simbachain.com/" if not set
3. AUTH_ENDPOINT defaults to "/o/" if not set
4. BASE_API_URL defaults to "https://simba-dev-api.platform.simbachain.com/" if not set

If you would rather set environment variables, then you will need to set:
|variable|default|additional notes|
|---|---|---|
|LIBSIMBA_BASE_API_URL|`https://simba-dev-api.platform.simbachain.com/`||
|LIBSIMBA_AUTH_FLOW|`client_credentials`|Can be one of: `pkce, client_credentials, or password`|
|LIBSIMBA_AUTH_APP_CLIENT_SECRET|`None`|This must be set if using `client_credentials`|
|LIBSIMBA_AUTH_APP_CLIENT_ID|`None`|This must be set if using `client_credentials`|
|LIBSIMBA_AUTH_BASE_URL|`https://simba-dev-api.platform.simbachain.com/`||
|LIBSIMBA_AUTH_ENDPOINT|`/o/`||

(Please see [setting up Django OAuth2 Toolkit client credentials flow](#SETTING-UP-FOR-DJANGO-OAUTH2-CLIENT-CREDENTIALS-FLOW) for an example on how to setup for Django OAuth2 authentication.)

### Keycloak Authentication
If you are using the Keycloak authentication flow, you will need to set the following environment variables so that the SDK can make auth requests and interact with the SIMBA Blocks platform.

|variable|default|additional notes|
|---|---|---|
|LIBSIMBA_BASE_API_URL|`https://api.sep.dev.simbachain.com`||
|LIBSIMBA_AUTH_FLOW|`client_credentials`|Can be one of: `pkce, client_credentials, or password`|
|LIBSIMBA_AUTH_APP_CLIENT_SECRET|`None`|Optional. This must be set if using `client_credentials`|
|LIBSIMBA_AUTH_APP_CLIENT_ID|`None`||
|LIBSIMBA_AUTH_APP_SCOPE|`api://<client_id>/scaas.access`||
|LIBSIMBA_AUTH_BASE_URL|`https://login.microsoftonline.com`||
|LIBSIMBA_AUTH_TENANT_ID|`None`||
|LIBSIMBA_AUTH_ENDPOINT|`/<tenant_id>/oauth2/v2.0/`||

(Please see [setting up keycloak client credentials flow](#SETTING-UP-FOR-KEYCLOAK-CLIENT-CREDENTIALS-FLOW) for an example on how to setup for keycloak authentication.)

## *Usage*
### *Instantiate the SIMBA Enterprise client*

```python
from libsimba.simba import Simba

simba = Simba() 
```

Or if you prefer to write asynchronous python code, then you can instantiate the async client:

```python
from libsimba.simba import SimbaAsync

simba_async = SimbaAsync()
```

All method signatures for both clients are exactly the same. The only difference being that most async client methods will return a coroutine. The two most accepted ways to write asynchronous python code is to either use `asyncio` or the `async/await` syntax. See example below:

```python
import asyncio

# Using asyncio
apps = asyncio.run(simba_async.list_applications())
# .. do something with apps

# Using async/await
class Example:
    async def do_something(self):
        apps = await simba_async.list_applications()
        # .. do something with apps
```

### *List all SIMBA applications available to your user*
```python
simba.list_applications()
```

Sample output:
```
[{'id': '51974f7a-6076-46c3-a37b-cb948f3e3642', 'display_name': 'My Application', 'name': 'myapi', 'created_on': '2019-12-16T10:00:00Z', 'components': [{'id': 'fd3d9987-fc1e-4d95-8aef-cec18b27f949', 'api_name': 'fabcar-test1', 'created_on': '2021-11-16T17:16:55.265625Z', 'updated_on': '2021-11-16T17:16:55.265635Z'}, {'id': 'ff271d8c-760f-4958-87d7-7c66cd626be0', 'api_name': 'myapi', 'created_on': '2019-12-16T10:00:00Z', 'updated_on': '2020-05-30T10:00:00Z'}], 'organisation': {'id': '51974f7a-6076-46c3-a37b-cb948f3e3641', 'display_name': 'Simbachain', 'name': 'org-1'}, 'metadata': None, 'openapi': 'http://localhost:8000/v2/apps/myapi/'}]
```

Please note the field `name` in the response. The `name` field is used as the parameter for application specific method calls.

### *Use the SearchFilter class to filter the list of results*
All methods returning a python list may be filtered using the SearchFilter class. Here is an example:
```python
from libsimba import SearchFilter

apps = simba.list_applications(
    search_filter=SearchFilter(name__contains='myappname')
    )
```

The SearchFilter may be constructed using [Django's Field Lookup Syntax](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)

### *List all contracts for a given SIMBA application*
```python
simba.list_contracts("myapi")
```

Sample output:
```
 [{'id': 'fd3d9987-fc1e-4d95-8aef-cec18b27f949', 'artifact': {'id': '602d946e-a342-41d6-95f9-19ef8709b13a', 'created_on': '2021-11-16T17:16:55.249408Z', 'updated_on': '2021-11-16T17:16:55.249418Z', 'name': 'FabCar'}, 'has_assets': False, 'blockchain': 'fabric', 'blockchain_type': 'fabric', 'storage': 'no_storage', 'storage_container': 'fabcar-test1', 'created_on': '2021-11-16T17:16:55.265625Z', 'updated_on': '2021-11-16T17:16:55.265635Z', 'address': 'basic', 'version': None, 'display_name': 'fabcar-test1', 'api_name': 'fabcar-test1', 'organisation': '51974f7a-6076-46c3-a37b-cb948f3e3641', 'contract_type': 'SINGLETON', 'asset_type': 'fabcar-test1', 'state': 'No Deployment Info'}]
```

Please note the `api_name` field. The `api_name` field is used as the parameter for contract specific method calls.

### *Get info on the contract method calls and data types*
```python
simba.list_contract_info("myapi", "fabcar-test1")
```

Sample output:
```
{'contract': {'name': 'FabCar', 'enums': {}, 'types': {'Car': {'components': [{'name': 'docType', 'type': 'string'}, {'name': 'color', 'type': 'string'}, {'name': 'make', 'type': 'string'}, {'name': 'model', 'type': 'string'}, {'name': 'owner', 'type': 'string'}]}}, 'assets': {}, 'events': {}, 'source': {'lang': 'hlfts', 'version': '2.2.0'}, 'methods': {'queryCar': {'emits': [], 'params': [{'name': 'carNumber', 'type': 'string'}], 'returns': [{'type': 'string'}], 'accessor': True, 'visibility': 'public'}, 'createCar': {'emits': [], 'params': [{'name': 'carNumber', 'type': 'string'}, {'name': 'make', 'type': 'string'}, {'name': 'model', 'type': 'string'}, {'name': 'color', 'type': 'string'}, {'name': 'owner', 'type': 'string'}], 'returns': [], 'accessor': False, 'visibility': 'public'}, 'initLedger': {'emits': [], 'params': [], 'returns': [], 'accessor': False, 'visibility': 'public'}, 'queryAllCars': {'emits': [], 'params': [], 'returns': [{'type': 'string'}], 'accessor': True, 'visibility': 'public'}, 'changeCarOwner': {'emits': [], 'params': [{'name': 'carNumber', 'type': 'string'}, {'name': 'newOwner', 'type': 'string'}], 'returns': [], 'accessor': False, 'visibility': 'public'}}, 'abstract': False, 'constructor': {'init_method': 'initLedger'}, 'inheritance': ['Contract']}, 'api_name': 'fabcar-test1', 'name': 'fabcar-test1', 'network': 'fabric', 'network_type': 'fabric', 'poa': False, 'faucet': None, 'simba_faucet': False}
```

The contract information provides details on methods, method parameters and return values. This is useful for constructing the inputs for your method call as demonstrated in the next example.

### *Example method call using the SDK*
```python
from libsimba.simba import Simba
import logging
log = logging.getLogger(__name__)

simba_app_name = 'myapi'
simba_app_contract = 'fabcar-test1'
simba_app_method = 'createCar'
simba_app_inputs = {
    'carNumber': 'VIN123345',
    'make': 'Volkswagon',
    'model': 'Beetle',
    'color': 'Yellow',
    'owner': 'Dale'
}

contract = simba.smart_contract_client(simba_app_name, simba_app_contract)
log.info('{} :: {}'.format(simba_app_name, simba_app_contract))

r = contract.call_method(simba_app_method, simba_app_inputs)
log.info(r)

r = contract.query_method(simba_app_method)
log.info(r)
```

### *Self-signing transaction*
It's also possible to sign the transaction with a locally loaded wallet.
```python
from libsimba.simba import Simba
from libsimba.simba_wallet import Wallet

simba = Simba()
wallet = Wallet()
wallet.generate_from_private_key("private_key")

contract = simba.smart_contract_client(simba_app_name, simba_app_contract)
unsigned_transaction = contract.call_method(simba_app_method, simba_app_inputs)
signed_transaction = wallet.sign_transaction(unsigned_transaction['raw_transaction'])

response = simba.submit_signed_transaction(
    app_id=simba_app_name, txn_id=unsigned_transaction['id'], txn=signed_transaction)
```

## *Use a class-based approach to interacting with your deployed smart contract*
LibSimba.py-platform has a module called the SimbaHintedContract that can be used to autogenerate a smart contract class containing method calls matching those of the given deployed smart contract. This makes it easier for developers to write applications as they no longer need write and then wire up functions for each smart contract method.

For a complete example on how to use the SimbaHintedContract module please see this [example notebook](https://github.com/SIMBAChain/libsimba.py-platform/blob/docs/notebooks/examples.ipynb).
------------------------------------------------

## *Appendix*

### *Setting up for Keycloak client credentials flow*

Create a new client in your Keycloak realm and set the following:

Access Type = confidential\
Service Accounts Enabled = ON

Save the client. Navigate to the Credentials tab and copy the client secret. \
Assuming that your realm is named `sep` and that the client is named `sep-client-credentials`, here is an example of how you would configure your environment:

```
export LIBSIMBA_AUTH_APP_CLIENT_SECRET="4c562d04-b9c8-4b49-95ff-b0aa2620154c"
export LIBSIMBA_AUTH_APP_CLIENT_ID="sep-client-credentials"
export LIBSIMBA_AUTH_APP_SCOPE="profile email"
export LIBSIMBA_AUTH_TENANT_ID="sep"
export LIBSIMBA_AUTH_BASE_URL="https://keycloak.example.com"
export LIBSIMBA_AUTH_ENDPOINT="auth/realms/sep/protocol/openid-connect/"
```
