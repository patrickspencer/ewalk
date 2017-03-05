# -*- coding: utf-8 -*-

import pprint
import datetime
import ewalk.settings
from yahoo_finance import Share
from ewalk.models import Quote, Symbol, dbsession

def create_sym(name):
    if not Symbol.exists(q['Symbol']):
        symbol = Symbol(
                 name = q['Symbol'],
                 )
        dbsession.add(symbol)
        dbsession.commit()

def get_sym_id(name):
    return dbsession.query(Symbol) \
              .filter(Symbol.name == name).first().id

def create_quote(quote):
    dt = datetime.datetime.strptime(quote['Date'], '%Y-%m-%d')
    if not Quote.exists(dt):
        quote = Quote(
                adj_close = q['Adj_Close'],
                open = q['Open'],
                close = q['Close'],
                high = q['High'],
                low = q['Low'],
                volume = q['Volume'],
                date = dt,
                symbol_id = get_sym_id(q['Symbol']),
                )
        dbsession.add(quote)
        dbsession.commit()

yahoo = Share('YHOO')

api_query = yahoo.get_historical('2016-01-01', '2017-03-05')
for q in api_query:
    create_sym(q['Symbol'])
    create_quote(q)


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

