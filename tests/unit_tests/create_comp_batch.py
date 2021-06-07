from libsimba.simba_hinted_contract import SimbaHintedContract

app_name = "newCompBatch"
contract_name = "newCompBatch"
base_api_url = 'https://api.sep.dev.simbachain.com/'
output_file = "generated_comp_batch.py"
sch = SimbaHintedContract(app_name, contract_name, base_api_url, output_file=output_file)