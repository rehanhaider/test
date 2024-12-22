import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.modify", "https://www.googleapis.com/auth/gmail.compose"]


def get_credentials():
    creds = None
    # time.
    if os.path.exists("mail/gmail/token.json"):
        creds = Credentials.from_authorized_user_file("mail/gmail/token.json", SCOPES)

    if os.path.exists("mail/gmail/token.json"):
        creds = Credentials.from_authorized_user_file("mail/gmail/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "mail/gmail/credentials.json", SCOPES
            )  # Replace with your credentials file
            creds = flow.run_local_server(port=0)
            print(creds)
        # Save the credentials for the next run
        with open("mail/gmail/token.json", "w") as token:
            token.write(creds.to_json())

    return creds


if __name__ == "__main__":
    creds = get_credentials()
    print(creds.to_json())
