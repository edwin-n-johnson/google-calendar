from __future__ import print_function
import datetime
import pickle
import os.path
import sys
import pprint
from googleapiclient.discovery import build

PICKLE = 'token.pickle'

def main():
    """Shows basic usage of the Google Calendar API.
    Creates an event
    """
    creds = None
    # The file token.pickle stores the user's access and refresh
    # tokens. This file is created in get-token.py
    if not os.path.exists(PICKLE):
        print('Token file ({}) does not exist. Run get-token.py first'.format(PICKLE))

    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, print an error and exit.
    if not creds or not creds.valid:
        print('Credentials token file is not valid. Run get-token.py to regenerate')
        sys.exit(1)

    # Get the Google Calendar service object
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow() # Use UTC so we don't have to worry about timezones
    start = now + datetime.timedelta(hours=1) # Start an hour from now
    end   = start + datetime.timedelta(hours=3) # 3 hours of skiing
    print('Creating an event to go skiing in 1 hour')
    new_event = {
        'summary': 'Go skiing!',
        'start': {
            'dateTime': start.isoformat() + 'Z' # 'Z' indicates UTC time
        },
        'end': {
            'dateTime': end.isoformat() + 'Z' # 'Z' indicates UTC time
        }
    }
    # Use the Calendar events object to insert a new event
    result = service.events().insert(calendarId='primary', body=new_event).execute()
    pprint.pprint(result)
    if result:
        print('Event created successfully')

if __name__ == '__main__':
    main()
