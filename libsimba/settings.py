import json
import os
from os.path import join, dirname
from decouple import config

DEBUG = True

PROJECT_PATH = dirname(__file__)

TEST_APP = "<set in local settings>"
TEST_CONTRACT = "<set in local settings>"
TEST_METHOD = "<set in local settings>"
TEST_INPUTS = []

# Use the env to override local_settings
# So load local_settings first
try:
    from libsimba.local_settings import *
except ModuleNotFoundError as e1:
    # Ignore if the local_settings file is missing
    pass

# Load from local_setting, then override with env var if present
TEST_APP = os.getenv('SIMBA_APP', TEST_APP)
TEST_CONTRACT = os.getenv('SIMBA_CONTRACT', TEST_CONTRACT)
TEST_METHOD = os.getenv('SIMBA_METHOD', TEST_METHOD)
test_input_json = os.getenv('SIMBA_INPUTS', None)
if test_input_json:
    TEST_INPUTS = json.loads(test_input_json)

# SCAAS API & Auth settings

# Options: client_credentials (Default), pkce, password
AUTH_FLOW = os.getenv('AUTH_FLOW', "client_credentials")

# [Optional] CLIENT_SECRET is only needed if using the client credentials flow.
CLIENT_SECRET = os.getenv('AZURE_AUTH_APP_CLIENT_SECRET', None)
CLIENT_ID = os.getenv('AZURE_AUTH_APP_CLIENT_ID', None)
SCOPE = os.getenv('AZURE_APP_ID', "api://{}/scaas.access".format(CLIENT_ID))

BASE_AUTH_URL = os.getenv('BASE_AUTH_URL', "https://login.microsoftonline.com")
TENANT_ID = os.getenv('AZURE_TENANT', None)
AUTH_ENDPOINT = os.getenv('AUTH_ENDPOINT', "/{}/oauth2/v2.0/".format(TENANT_ID))
BASE_API_URL = os.getenv('BASE_API_URL', "https://api.sep.dev.simbachain.com")

# using config library
# to use this approach, create a .env file in the same directory as this file:
# $ touch .env
# then set these variables using nano:
# $ nano .env
# then within nano:
# AZURE_AUTH_APP_CLIENT_SECRET=<value>
# AZURE_AUTH_APP_CLIENT_ID-<value>
# ...
USE_GETENV_OR_CONFIG = "<enter 'CONFIG' or 'GETENV' here>"

if USE_GETENV_OR_CONFIG == "CONFIG":
    CLIENT_SECRET = config('AZURE_AUTH_APP_CLIENT_SECRET', default = None)
    CLIENT_ID = config('AZURE_AUTH_APP_CLIENT_ID', default = None)

    BASE_AUTH_URL = config('BASE_AUTH_URL', default = "https://login.microsoftonline.com")
    TENANT_ID = config('AZURE_TENANT', default = None)
    SEP_RESOURCE_PRINCIPAL_ID= config('SEP_RESOURCE_PRINCIPAL_ID')
    SCOPE = config('AZURE_APP_ID', default = "api://{}/.default".format(SEP_RESOURCE_PRINCIPAL_ID))
    AUTH_ENDPOINT = config('AUTH_ENDPOINT', default = "/{}/oauth2/v2.0/".format(TENANT_ID))
    BASE_API_URL = config('BASE_API_URL', default = "https://api.sep.dev.simbachain.com")


