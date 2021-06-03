
from libsimba.simba_hinted_contract import SimbaHintedContract
import pprint
pprint = pprint.PrettyPrinter().pprint 


app_name = "TestSimbaHinted"
contract_name = "TestSimbaHinted"
base_api_url = 'https://api.sep.dev.simbachain.com/'
output_file = "generated_simba_hinted_contract.py"
sch = SimbaHintedContract(app_name, contract_name, base_api_url, output_file=output_file)
sch.write_contract()





