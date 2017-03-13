# -*- coding: utf-8 -*-

import datetime
from yahoo_finance import Share
from datetime import date, timedelta as td
from stockwalk.models import Quote, Company, dbsession

def get_company_id(symbol):
    return dbsession.query(Company).filter(Company.symbol == symbol).first().id

def create_quote(quote):
    date = datetime.datetime.strptime(quote['Date'], '%Y-%m-%d')
    if not Quote.exists(date, quote['Symbol']):
        q = Quote(
                adj_close = quote['Adj_Close'],
                open = quote['Open'],
                close = quote['Close'],
                high = quote['High'],
                low = quote['Low'],
                volume = quote['Volume'],
                date = date,
                company_id = get_company_id(quote['Symbol']),
                )
        dbsession.add(q)
        dbsession.commit()

#
# d1 = datetime.strptime(start_time, '%Y-%m-$d')
# d1 = datetime.strptime(end_time, '%Y-%m-$d')
#
# delta = d2 - d1
#
# for i in range(delta.days + 1):
#         print d1 + td(days=i)

def write_quotes_to_db(symbol):
    start_date = '2016-01-01'
    end_date = '2017-03-05'
    """ TODO: fix this to see if quote with date and symbol exists """
    if not Quote.symbol_exists(symbol):
        try:
            api_query = Share(symbol).get_historical(start_date, end_date)
        except AttributeError:
            print("Attribute error")
        for q in api_query:
            if q:
                create_quote(q)

companies = dbsession.query(Company).all()
for company in companies:
    write_quotes_to_db(company.symbol)
    print('Added quotes for ' + company.symbol + '; company_id: ' + str(company.id))
