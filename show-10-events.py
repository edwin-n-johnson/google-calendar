from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
PICKLE = 'token.pickle'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh
    # tokens. This file is created in get-token.py
    if not os.path.exists(PICKLE):
        print('Token file ({}) does not exist. Run get-token.py first'.format(PICKLE))

    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print('Credentials token file is not valid. Run get-token.py to regenerate')

    # Get the Google Calendar service object
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    # Use the Calendar events object to retreive the events
    #calId = 'primary'
    calId = 'ins31cvsv7fcmeu9s8ahnsc60c@group.calendar.google.com'
    events_result = service.events().list(calendarId=calId, timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()
