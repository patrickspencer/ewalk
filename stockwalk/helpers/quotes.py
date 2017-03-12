import datetime
from sqlalchemy import exists
from stubhub import apiqueries
from stockwalk.helpers import timezones
from stockwalk.models import Quote, dbsession

def add_quote_to_db(quotes):
    """
    :params quotes:
    """
    for quote in quotes:
        if not event_exists(quote['datetime_accessed']):
            dbsession.add(objectify_event(event))
    dbsession.commit()
