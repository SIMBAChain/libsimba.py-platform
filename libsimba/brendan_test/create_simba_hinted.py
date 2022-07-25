from libsimba.simba_hinted_contract import SimbaHintedContract
app_name = "BrendanTestApp"
contract_name = "test_contract_vt3"
# base_api_url = 'https://api.sep.dev.simbachain.com/'
output_file = "test_contract_vt3.py"
contract_class_name = "TestContractVT3"

shc = SimbaHintedContract(
    app_name, 
    contract_name, 
    contract_class_name=contract_class_name,
    output_file=output_file)
shc.write_contract()
