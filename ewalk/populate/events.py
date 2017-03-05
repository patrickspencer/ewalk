import pprint
from stubhub import apiqueries
from stubhub.helpers.events import add_events_to_db

pp = pprint.PrettyPrinter(indent=4)

event_response = apiqueries.search_events(query='', groupingName='NBA Regular', start=1)
# if event_response.json()['numfound'] > 500:
#
if event_response.status_code == 200:
    events = event_response.json()['events']
    add_events_to_db(events)
else:
    # raise error if response is no 200
    event_response.raise_for_status()
