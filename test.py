# -*- coding: utf-8 -*-

from ewalk.models import dbsession
from ewalk import create_quote
from yahoo_finance import Share
from ewalk.models import Quote, Symbol, dbsession

print(dbsession.query(Symbol).filter(Symbol.name == 'YHOO').first().id)
