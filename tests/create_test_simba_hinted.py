from libsimba.simba_hinted_contract import SimbaHintedContract
app_name = "TestSimbaHinted"
contract_name = "TestSimbaHinted"
base_api_url = 'https://api.sep.dev.simbachain.com/'
output_file = "test_simba_hinted.py"
contract_class_name = "TestSimbaHinted"

sch = SimbaHintedContract(
    app_name, 
    contract_name, 
    contract_class_name=contract_name, 
    base_api_url=base_api_url, 
    output_file=output_file)