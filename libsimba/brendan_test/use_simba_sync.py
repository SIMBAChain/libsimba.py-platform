from libsimba.simba_sync import SimbaSync
import logging
log = logging.getLogger(__name__)

simba_app_name = 'BrendanTestApp'
simba_app_contract = 'simplenum_vbbt11'
simba_app_method = 'setNum'
simba_app_inputs = {
    '_ourNum': 99,
}

simba_sync = SimbaSync()
print(simba_sync.base_api_url)
contract = simba_sync.smart_contract_client(simba_app_name, simba_app_contract)
log.info('{} :: {}'.format(simba_app_name, simba_app_contract))

r = contract.call_method(simba_app_method, simba_app_inputs)
log.info(r)

# r = contract.query_method(simba_app_method)
# log.info(r)