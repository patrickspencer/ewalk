# -*- coding: utf-8 -*-

import datetime
from yahoo_finance import Share
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

def write_quotes_to_db(symbol):
    start_date = '2016-01-01'
    end_date = '2017-03-05'
    api_query = Share(symbol).get_historical(start_date, end_date)
    for q in api_query:
        create_quote(q)

companies = dbsession.query(Company).all()
for company in companies:
    write_quotes_to_db(company.symbol)
    print('Added quotes for ' + company.symbol + '; company_id: ' + str(company.id))
