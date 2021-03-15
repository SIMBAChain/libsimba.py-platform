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
from libsimba.settings import CLIENT_ID, SCOPE, BASE_AUTH_URL, AUTH_ENDPOINT
from libsimba.utils import build_url


class Auth:

    access_token=None

    @staticmethod
    def main():
        Auth.login()
    
    @staticmethod
    def login():
        if Auth._is_authenticated():
            return Auth.access_token

        [code_verifier, code_challenge] = Auth._prepare_challenge()

        thread = _thread.start_new_thread(Auth.start_server, (code_verifier,))
        sleep(1)

        query_params = {
            "response_type": "code",
            "client_id": CLIENT_ID,
            "redirect_uri": "http://localhost:7201", 
            "scope": SCOPE, 
            "code_challenge": code_challenge,
            "code_challenge_method": "S256"
        }

        print(build_url(BASE_AUTH_URL, "{}authorize".format(AUTH_ENDPOINT), query_params))

        while Auth.access_token is None:
            pass
        
        return Auth.access_token

    @staticmethod
    def start_server(code_verifier):
        class CallbackHandler(BaseHTTPRequestHandler):
            #Handler for the GET requests
            def do_GET(self):
                if re.match(r'', self.path):
                    try:
                        code = (parse_qs(self.path.split("?")[1]))['code'][0]
                        self.write_ok()
                        self.get_token(code)
                    except:
                        pass

            def write_ok(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write("OK <p> You may close this window and return to shell :) </p>".encode())
        
            def get_token(self, code):
                body = {
                    "code": code,
                    "code_verifier": code_verifier,
                    "client_id": CLIENT_ID,
                    "redirect_uri": "http://localhost:7201",
                    "grant_type": "authorization_code"
                }

                auth_url = build_url(BASE_AUTH_URL, AUTH_ENDPOINT, {})
                
                r = requests.post("{}token".format(auth_url), data=body, headers={'origin': 'http://localhost:7201'})
                
                access_token = r.json()['access_token']

                with open('./.token', 'w') as fd:
                    fd.write(access_token)
                
                Auth.access_token = access_token
                
        server = HTTPServer(('', 7201), CallbackHandler)
        server.serve_forever()

    @staticmethod
    def _is_authenticated():
        if Auth.access_token is not None:
            return True
        
        if os.path.exists('./.token'):
            with open('./.token', 'r') as fd:
                access_token = fd.read()
                # whoami_url = build_url(BASE_API_URL, "user/whoami/", {})
                try:
                    # r = requests.get(whoami_url, headers={'Authorization': "Bearer {}".format(access_token)})
                    # if r.status_code != 200:
                        # return False
                    Auth.access_token = access_token
                    return True
                except:
                    return False

    @staticmethod
    def _prepare_challenge():
        random = secrets.token_bytes(64)
        code_verifier = base64.b64encode(random, b'-_').decode().replace('=', '')

        m = hashlib.sha256()
        m.update(code_verifier.encode())
        d = m.digest()
        code_challenge = base64.b64encode(d, b'-_').decode().replace('=', '')
        return [code_verifier, code_challenge]

if __name__ == '__main__':
    Auth.main()
