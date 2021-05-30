
from libsimba.simba_hinted_contract import SimbaHintedContract
import os 
import pprint
pprint = pprint.PrettyPrinter().pprint 


# not a proper test - just demonstrating instantiating hinted class object 
# using different metadata.json files
wDir = os.path.dirname(__file__)

relPath = 'data/app_md.json'
metadata = os.path.join(wDir, relPath)
output_file = 'app_md_contract.py'
app_name = "app_md_app"
scc = SimbaHintedContract(metadata, app_name, output_file = output_file)
scc.write_contract()
# print(scc.contract_name)


relPath = 'data/app_md_2.json'
metadata = os.path.join(wDir, relPath)
output_file = "app_md_2_contract.py"
app_name = "app_md_2_app"
scc = SimbaHintedContract(metadata, app_name, output_file = output_file)
scc.write_contract()
# print(scc.contract_name)

relPath = 'data/app_md_3.json'
metadata = os.path.join(wDir, relPath)
output_file = "app_md_3_contract.py"
app_name = "app_md_3_app"
scc = SimbaHintedContract(metadata, app_name, output_file=output_file)
scc.write_contract()
# print(scc.contract_name)



