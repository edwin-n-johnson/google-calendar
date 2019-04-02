from __future__ import print_function
import datetime
import pickle
import os.path
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
PICKLE = 'token.pickle'
CREDENTIALS = 'credentials.json'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(PICKLE):
        print('Pickled token file found ' + PICKLE)
        print('Verifying...')
        with open(PICKLE, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS):
                print('Missing credentials file: ' + CREDENTIALS)
                print('Visit the following URL to generate it: https://developers.google.com/calendar/quickstart/python')
                sys.exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(PICKLE, 'wb') as token:
            pickle.dump(creds, token)

        if creds:
            print('Credentials created and pickled into ' + PICKLE)

    if creds and creds.valid:
        print('Credentials token file is ready: ' + PICKLE)
    else:
        print('Error generating credentials')

if __name__ == '__main__':
    main()
