
from libsimba.simba_hinted_contract import SimbaHintedContract
import os 
import pprint
pprint = pprint.PrettyPrinter().pprint 

# new interface used here - just providing example of writing contract as class object in "test_simba_output.py"
app_name = "TestSimbaHinted"
contract_name = "TestSimbaHinted"
base_api_url = 'https://api.sep.dev.simbachain.com/'
output_file = "generated_simba_hinted_contract.py"
sch = SimbaHintedContract(app_name, contract_name, base_api_url, output_file=output_file)
sch.write_contract()





