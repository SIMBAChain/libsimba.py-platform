import os

from os.path import join, dirname

DEBUG = False

PROJECT_PATH = dirname(__file__)

#SCAAS API & Auth settings
CLIENT_ID = os.getenv('CLIENT_ID', '11cbd388-342e-4d19-a6ca-97aa56deaad3')
SCOPE = "api://{}/scaas.access".format(CLIENT_ID)

BASE_AUTH_URL = "https://login.microsoftonline.com"
AUTH_ENDPOINT = "/97fd3cb6-823b-4578-ab45-226a5925ce05/oauth2/v2.0/"

BASE_API_URL = "https://api.sep.dev.simbachain.com"
# APP_ENDPOINT = "/v2/apps/vipart/contract/vipart_oem_v2/"
