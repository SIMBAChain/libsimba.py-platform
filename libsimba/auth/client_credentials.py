import re
import os
import _thread
import base64
import hashlib
import secrets
import requests
from urllib.parse import parse_qs
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer
from libsimba.settings import CLIENT_ID, CLIENT_SECRET, SCOPE, BASE_AUTH_URL, AUTH_ENDPOINT, BASE_API_URL
from libsimba.utils import build_url


class ClientCredentials:

    access_token=None

    @staticmethod
    def main():
        ClientCredentials.login()
    
    @staticmethod
    def login():
        if ClientCredentials._is_authenticated():
            return ClientCredentials.access_token

        payload = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": SCOPE
        }

        access_token = None
        try:
            auth_url = build_url(BASE_AUTH_URL, "{}token".format(AUTH_ENDPOINT), {})
            r = requests.post(auth_url, data=payload, allow_redirects=True)    

            access_token = r.json()['access_token']
        except Exception as e:
            print(e)
            return None


        if access_token is not None:
            with open('./.token', 'w') as fd:
                fd.write(access_token)
        
        ClientCredentials.access_token = access_token

        return access_token

    @staticmethod
    def _is_authenticated():
        if ClientCredentials.access_token is not None:
            return True
        
        if os.path.exists('./.token'):
            with open('./.token', 'r') as fd:
                access_token = fd.read()
                whoami_url = build_url(BASE_API_URL, "user/whoami/", {})
                try:
                    r = requests.get(whoami_url, headers={'Authorization': "Bearer {}".format(access_token)})
                    if r.status_code != 200:
                        return False
                    ClientCredentials.access_token = access_token
                    return True
                except:
                    return False

if __name__ == '__main__':
    ClientCredentials.main()
