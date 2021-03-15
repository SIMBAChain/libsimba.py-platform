import requests
from libsimba.auth import Auth
from libsimba.decorators import auth_required
from libsimba.utils import build_url
from libsimba.settings import BASE_API_URL, DEBUG

class Simba:
    def __init__(self, app_endpoint):
        self.app_endpoint = app_endpoint

    # TEST method
    @staticmethod
    def main():
        simba = Simba("/v2/apps/testing/contract/simple/")
        user_info = simba.whoami()
        print(user_info)

    @auth_required
    def whoami(self, access_token):
        whoami_url = build_url(BASE_API_URL, "user/whoami/", {})
        r = requests.get(whoami_url, headers={'Authorization': "Bearer {}".format(access_token)})
        return r.json()

if DEBUG is True and __name__ == "__main__":
    Simba.main()
