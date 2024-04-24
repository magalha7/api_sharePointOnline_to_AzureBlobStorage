import os
from msal import ConfidentialClientApplication
from decouple import config


TENANT_ID = config('sharepoint_tenant_id')
CLIENT_ID = config('sharepoint_client_id')
CLIENT_SECRET = config('sharepoint_client_secret_value')

def auth():

    msal_authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    msal_scope = ["https://graph.microsoft.com/.default"]

    msal_app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=msal_authority
    )

    result = msal_app.acquire_token_silent(
        scopes=msal_scope,
        account=None
    )

    if not result:
         result = msal_app.acquire_token_for_client(scopes=msal_scope)

    if "access_token" in result:
         access_token = result["access_token"]
         return access_token
    else:
         raise Exception("No Access Token found or Token has expired in Azure AD")
