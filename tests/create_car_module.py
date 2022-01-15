from libsimba.simba_hinted_contract import SimbaHintedContract
app_name = "titles"
base_api_url = 'https://api.sep.dev.simbachain.com/'

contract_names = [
  "DMVImplementationM8",
  "RegistrationERC721M8",
  "CertificateOfSalvageERC721M8",
  "TitleERC721M8",
  "CarERC721M8",
  "DMVInterfaceM8",
  "DMVUpgradableM8",
  ]
contract_file_names = [ctr_name.lower() for ctr_name in contract_names]

for contract_name, file_name in list(zip(contract_names, contract_file_names)):
  sch = SimbaHintedContract(
    app_name,
    contract_name,
    contract_class_name=contract_name,
    base_api_url=base_api_url,
    output_file=f'./car_contracts/{file_name}.py'
  )
