from __future__ import print_function
import datetime
import pickle
import os.path
import sys
import pprint
import argparse
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

    # Parse the args
    parser = argparse.ArgumentParser()
    parser.add_argument("what")
    parser.add_argument("when")
    parser.add_argument("duration")
    args = parser.parse_args()

    # Handle when
    when_start = datetime.datetime.strptime(args.start, "%m-%d-%Y")
    when_end = when_start + int(args.duration)
    when_start = str(when_start.date())
    when_end = str(when_end.date())

    summary = args.what

    # Call the Calendar API
    print('Creating an event {} from {} - {}'.format(args.what, when_start, when_end))
    new_event = {
        'summary': summary,
        'start': {
            'date': when_start
        },
        'end': {
            'date': when_end
        },
        'transparency': "transparent"
    }
    # Use the Calendar events object to insert a new event
    # calId = 'primary'
    cal_id = 'ins31cvsv7fcmeu9s8ahnsc60c@group.calendar.google.com'
    result = service.events().insert(calendarId=cal_id, body=new_event).execute()
    print()
    pprint.pprint(result)
    if result:
        print('Event created successfully')


if __name__ == '__main__':
    main()
