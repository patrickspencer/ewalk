# -*- coding: utf-8 -*-

from ewalk import models
import pprint
import settings
import datetime
from yahoo_finance import Share

yahoo = Share('YHOO')
# print(yahoo.get_open())
# print(yahoo.get_price())
# print(yahoo.get_trade_datetime())
# print(yahoo.get_historical('2014-04-25', '2014-04-26'))

api_query = yahoo.get_historical('2017-03-01', '2017-03-05')
query = api_query[0]
# quote = Quote()

# for snapshot in api_query:
#     quote =
#     snapshot['Adj_Close']

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(api_query)

# def add_quote_to_db(quotes):
#     """
#     :params events: A list of quotes, not a query_result. This is what you get
#     when you do the following:
#
#         stubhub_response = apiqueries.search_events(query='Timberwolves',
#                 groupingName='NBA Regular')
#         events = stubhub_response.json()['events']
#
#     """
#     for quote in quotes:
#         if not event_exists(event['id']):
#             dbsession.add(objectify_event(event))
#     dbsession.commit()

