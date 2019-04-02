# google-calendar
## References
 - https://developers.google.com/calendar/quickstart/python
 - https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/
## Steps
 1. Follow step 1 of the Python Quickstart. This will create some credentials for your new project. Download the credentials.json file for your new project.
 2. Install the google api and client modules via step 2 of the Python Quickstart
 3. There are 3 extra scripts in addition to the standard quickstart.py:
    - **get-token.py** - Requests authentication to view and modify the calendar. Generates the token.pickle file needed by the following scripts
    - **show-10-events.py** - Shows the next 10 upcoming events
    - **create-event.py** - Creates a new event that starts 1 hour from now and ends 3 hours later
