from libsimba.auth import Auth

def auth_required_static(func):
    def _auth_required_fn_wrapper(*args):
        access_token = Auth.login()
        return func({'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper

def auth_required(func):
    def _auth_required_fn_wrapper(self, *args):
        access_token = Auth.login()
        return func(self, {'Authorization': "Bearer {}".format(access_token)}, *args)
    return _auth_required_fn_wrapper