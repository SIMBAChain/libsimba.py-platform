import requests
from requests.auth import HTTPBasicAuth
from libsimba.auth import AuthProvider
import base64
from libsimba.settings import (
    CLIENT_ID,
    CLIENT_SECRET,
    SCOPE,
    BASE_AUTH_URL,
    AUTH_ENDPOINT,
    BASE_API_URL,
)
from libsimba.utils import build_url, save_token, get_saved_token

import logging

log = logging.getLogger(__name__)


class ClientCredentials(AuthProvider):

    access_token = None

    @staticmethod
    def main():
        ClientCredentials.login()

    @staticmethod
    def login():
        if ClientCredentials._is_authenticated():
            return ClientCredentials.access_token
        log.info("Failed ClientCredentials._is_authenticated()")

        credential = f'{CLIENT_ID}:{CLIENT_SECRET}'
        encoded_credential = base64.b64encode(credential.encode('utf-8'))

        payload = {
            "grant_type": "client_credentials",
        }

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
            "Authorization": f"Basic {encoded_credential}"
        }

        access_token = None
        try:
            log.info("Redoing auth")
            auth_url = build_url(BASE_AUTH_URL, f"{AUTH_ENDPOINT}token/", {})
            basic_auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
            r = requests.post(auth_url, auth=basic_auth, headers=headers, data=payload, allow_redirects=True)
            r.raise_for_status()
            access_token = r.json()["access_token"]
        except Exception as e:
            log.error(e)
            return None

        if access_token is not None:
            save_token(client_id=CLIENT_ID, token_data=r.json())

        ClientCredentials.access_token = access_token

        return access_token

    @staticmethod
    def _is_authenticated():
        if ClientCredentials.access_token is not None:
            return True
        try:
            access_token = get_saved_token(CLIENT_ID)["access_token"]
        except:
            return False

        whoami_url = build_url(BASE_API_URL, "/user/whoami/", {})
        try:
            r = requests.get(
                whoami_url, headers={"Authorization": f"Bearer {access_token}"}
            )
            if r.status_code != 200:
                return False
            ClientCredentials.access_token = access_token
            return True
        except:
            return False


if __name__ == "__main__":
    ClientCredentials.main()
