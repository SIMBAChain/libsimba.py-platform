from libsimba.auth.pkce import Pkce
from libsimba.auth.client_credentials import ClientCredentials
from libsimba.settings import CLIENT_ID, CLIENT_SECRET, SCOPE, AUTH_FLOW, TENANT_ID

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