from libsimba.auth import Pkce
from libsimba.auth import ClientCredentials
from libsimba.settings import AUTH_FLOW

_ = {
  'pkce': Pkce,
  'client_credentials': ClientCredentials
}

auth_flow = AUTH_FLOW.lower()

def auth_required_static(func):
    def _auth_required_fn_wrapper(*args):
        access_token = _[auth_flow].login()
        return func({'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper

def auth_required(func):
    def _auth_required_fn_wrapper(self, *args):
        access_token = _[auth_flow].login()
        return func(self, {'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper