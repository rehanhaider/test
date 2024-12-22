from msal import PublicClientApplication
import json


config = json.load(open("mail/outlook/config.json"))


# def confidential_client_application():

#     app = ConfidentialClientApplication(
#         config["client_id"],
#         authority=f"https://login.microsoftonline.com/{config['tenant_id']}",
#         client_credential=config["client_secret"],
#     )

#     # Initialize result variable to hold the token response
#     result = None

#     # For confidential client applications, use the .default scope
#     scopes = ["https://graph.microsoft.com/.default"]

#     # Try to get token silently first
#     result = app.acquire_token_silent(scopes, account=None)

#     if not result:
#         print("No suitable token exists in cache. Let's get a new one from Azure AD.")
#         result = app.acquire_token_for_client(scopes=scopes)

#     print(result)
#     if "access_token" in result:
#         print("Successfully acquired token")
#     else:
#         print(f"Error acquiring token: {result.get('error')}")
#         print(f"Error description: {result.get('error_description')}")


def public_client_application():
    # This is working
    scopes = ["User.Read", "Mail.Read", "Mail.ReadWrite"]
    app = PublicClientApplication(
        config["client_id"],
        authority="https://login.microsoftonline.com/common",
    )

    flow = app.initiate_device_flow(scopes=scopes)
    print(flow)
    result = app.acquire_token_by_device_flow(flow)
    print(result)


def get_access_token_using_refresh_token():
    with open("mail/outlook/tokens.json") as f:
        tokens = json.load(f)
    print(tokens["refresh_token"])

    scopes = ["User.Read", "Mail.Read", "Mail.ReadWrite"]
    app = PublicClientApplication(
        config["client_id"],
        authority="https://login.microsoftonline.com/common",
    )

    result = app.acquire_token_by_refresh_token(refresh_token=tokens["refresh_token"], scopes=scopes)
    print(result)


get_access_token_using_refresh_token()
