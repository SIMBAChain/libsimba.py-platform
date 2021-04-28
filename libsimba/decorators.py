from libsimba.auth.pkce import Pkce
from libsimba.auth.client_credentials import ClientCredentials
from libsimba.settings import AUTH_FLOW
from libsimba.settings import CLIENT_ID, CLIENT_SECRET, SCOPE, AUTH_FLOW, TENANT_ID

_ = {
  'pkce': Pkce,
  'client_credentials': ClientCredentials
}

auth_flow = AUTH_FLOW.lower()


def auth_required_static(func):
    def _auth_required_fn_wrapper(*args):
        try:
            check_creds()
        except Exception as e1:
            raise e1
        access_token = _[auth_flow].login()
        return func({'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper


def auth_required(func):
    def _auth_required_fn_wrapper(self, *args):
        try:
            check_creds()
        except Exception as e1:
            raise e1
        access_token = _[auth_flow].login()
        return func(self, {'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper


def check_creds():
    if (
            CLIENT_ID is None or SCOPE is None or TENANT_ID is None or
            (AUTH_FLOW == 'client_credentials' and CLIENT_SECRET is None)
    ):
        raise Exception(
            """
            Could not get Auth token
            Please ensure that all of the following environment variables are set:
  
            AZURE_AUTH_APP_CLIENT_SECRET
            AZURE_AUTH_APP_CLIENT_ID
            AZURE_APP_ID
            AZURE_TENANT
            """
        )
