
from libsimba.simba_hinted_contract import SimbaHintedContract
import os 
import pprint
pprint = pprint.PrettyPrinter().pprint 


# not a proper test - just demonstrating instantiating hinted class object 
# using different metadata.json files
wDir = os.path.dirname(__file__)

relPath = 'data/app_md.json'
metadata = os.path.join(wDir, relPath)
outputFile = 'app_md_contract.py'
appName = "app_md_app"
scc = SimbaHintedContract(metadata, appName, outputFile = outputFile)
scc.write_contract()


relPath = 'data/app_md_2.json'
metadata = os.path.join(wDir, relPath)
outputFile = "app_md_2_contract.py"
appName = "app_md_2_app"
scc = SimbaHintedContract(metadata, appName, outputFile = outputFile)
scc.write_contract()

relPath = 'data/app_md_3.json'
metadata = os.path.join(wDir, relPath)
outputFile = "app_md_3_contract.py"
appName = "app_md_3_app"
scc = SimbaHintedContract(metadata, appName, outputFile=outputFile)
scc.write_contract()


