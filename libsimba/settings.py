import os

from os.path import join, dirname

DEBUG = False

PROJECT_PATH = dirname(__file__)

#SCAAS API & Auth settings

# Options: client_credentials (Default), pkce, password
AUTH_FLOW = "client_credentials" 

# [Optional] CLIENT_SECRET is only needed if using the client credentials flow.
CLIENT_SECRET = os.getenv('CLIENT_SECRET', '<set in local settings>')
CLIENT_ID = os.getenv('CLIENT_ID', '11cbd388-342e-4d19-a6ca-97aa56deaad3')
SCOPE = "api://{}/scaas.access".format(CLIENT_ID)

BASE_AUTH_URL = "https://login.microsoftonline.com"
TENANT_ID = "<set in local settings>"
AUTH_ENDPOINT = "/{}/oauth2/v2.0/".format(TENANT_ID)

BASE_API_URL = "https://api.sep.dev.simbachain.com"

TEST_APP = "<set in local settings>"
TEST_CONTRACT = "<set in local settings>"
TEST_METHOD = "<set in local settings>"
TEST_INPUTS = []

try:
    from libsimba.local_settings import *
except:
    pass