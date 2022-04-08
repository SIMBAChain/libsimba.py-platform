from libsimba import Simba, SimbaAsync, SearchFilter
import logging
import asyncio
log = logging.getLogger(__name__)

# TEST_APP = 'myapi'
# TEST_CONTRACT = 'fabcar-test1'

# TEST_METHOD = 'createCar'

# TEST_INPUTS = {
#   "carNumber": "347",
#   "color": "Bluish",
#   "make": "Toyota",
#   "model": "Camry",
#   "owner": "Buck"
# }

simba = Simba()

whoami = simba.whoami()
log.info(whoami)

apps = simba.list_applications()
log.info(apps)

# simba_contract = simba.smart_contract_client('myapi', 'fabcar-test1')
# contract = simba.get_contract(TEST_APP, TEST_CONTRACT)
# log.info('{} :: {} :: {}'.format(BASE_API_URL, TEST_APP, TEST_CONTRACT))

# r = contract.submit_method(TEST_METHOD, TEST_INPUTS)
# log.info(r.text)
# assert (r.status_code >= 200 and r.status_code <= 299)
# log.info(r.json())

# r = contract.query_method(TEST_METHOD)
# assert (r.status_code >= 200 and r.status_code <= 299)
# log.info(r.json())


# r = simba.list_contract_info("myapi", "fabcar-test1")
# log.info(r)

# simba_app_name = 'myapi'
# simba_app_contract = 'fabcar-test1'
# simba_app_method = 'createCar'
# simba_app_inputs = {
#     'carNumber': 'VIN123345',
#     'make': 'Volkswagon',
#     'model': 'Beetle',
#     'color': 'Yellow',
#     'owner': 'Dale'
# }

# contract = simba.smart_contract_client(simba_app_name, simba_app_contract)
# log.info('{} :: {}'.format(simba_app_name, simba_app_contract))

# r = contract.call_method(simba_app_method, simba_app_inputs)
# log.info(r)

# r = contract.query_method(simba_app_method)
# log.info(r)

# app_name = r.json()['results'][0]['name']
# r = simba.list_contracts(app_name)
# log.info(r.json())

# contract_api_name = r.json()['results'][0]['api_name']
# r = simba.list_contract_info(app_name, contract_api_name)
# log.info(r.json())

# simba_app_name = 'myapi'
# simba_app_contract = 'fabcar-test1'
# simba_app_method = 'createCar'
# simba_app_inputs = {
#     'carNumber': 'VIN123345',
#     'make': 'Toyota',
#     'model': 'Beetle',
#     'color': 'Yellow',
#     'owner': 'Dale'
# }
# r = simba_contract.submit_method_async('createCar', simba_app_inputs)
# r = simba.submit_contract_method('myapi', 'fabcar-test1', 'createCar', simba_app_inputs)
# log.info(r)

# simba = Simba()
# contract = simba.get_contract(simba_app_name, simba_app_contract)
# log.info('{} :: {}'.format(simba_app_name, simba_app_contract))

# r = contract.submit_method(simba_app_method, simba_app_inputs)
# log.info(r.text)
# assert (r.status_code >= 200 and r.status_code <= 299)
# log.info(r.json())

# r = contract.query_method(simba_app_method)
# assert (r.status_code >= 200 and r.status_code <= 299)
# log.info(r.json())
