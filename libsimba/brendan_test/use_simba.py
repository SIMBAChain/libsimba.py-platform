from libsimba.simba import Simba
import logging
log = logging.getLogger(__name__)
import asyncio

# simba_app_name = 'BrendanTestApp'
# simba_app_contract = 'simplenum_vbbt11'
# simba_app_method = 'setNum'
# simba_app_inputs = {
#     '_ourNum': 99,
# }

async def main():
    simba = Simba()
    # print(simba.base_api_url)
    # contract = simba.smart_contract_client(simba_app_name, simba_app_contract)
    # log.info('{} :: {}'.format(simba_app_name, simba_app_contract))

    # r = await contract.call_method(simba_app_method, simba_app_inputs)
    # log.info(r)
    # http://localhost:3000/v2/apps/BrendanTestApp/contract/test_contract_vt3/bundle/dde4[…]af63f18eca3ddec1220240718bfc1b4a71c186da3dd5ffdfde0/manifest/
    app_id = "BrendanTestApp"
    contract_name = "test_contract_vt3"
    bundle_hash = "dde43af42fb3faf63f18eca3ddec1220240718bfc1b4a71c186da3dd5ffdfde0"

    manifest = await simba.get_manifest_for_bundle_from_bundle_hash(
        app_id,
        contract_name,
        bundle_hash,
    )
    print(f'manifest:\n\n{manifest}')

    # r = contract.query_method(simba_app_method)
    # log.info(r)
asyncio.run(main())