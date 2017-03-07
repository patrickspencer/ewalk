import click
from yahoo_finance import Share
from ewalk import create_sym, create_quote
# from ewalk.models import Quote, Symbol, dbsession

@click.command()
@click.option('--symbol', default='YHOO', help='Symbol of stock market stock, ex: YHOO')
def write_quotes_to_db(symbol):
    api_query = Share(symbol).get_historical('2016-01-01', '2017-03-05')
    for q in api_query:
        create_sym(q['Symbol'])
        create_quote(q)

if __name__ == '__main__':
    write_quotes_to_db()

