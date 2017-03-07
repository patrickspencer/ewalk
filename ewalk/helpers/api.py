# -*- coding: utf-8 -*-

import click
import datetime
import ewalk.settings
from yahoo_finance import Share
from ewalk.models import Quote, Symbol, dbsession

def create_sym(symbol):
    if not Symbol.exists(symbol):
        symbol = Symbol(
                 name = symbol,
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

@click.command()
@click.option('--symbol', default='YHOO', help='Symbol of stock market stock, ex: YHOO')
def write_quotes_to_db(symbol):
    api_query = Share(symbol).get_historical('2016-01-01', '2017-03-05')
    for q in api_query:
        create_sym(q['Symbol'])
        create_quote(q)

if __name__ == '__main__':
    write_quotes_to_db()
