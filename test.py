# -*- coding: utf-8 -*-

from ewalk.models import dbsession
from ewalk import create_quote
from yahoo_finance import Share
from stockwalk.models import Quote, Company, dbsession

print(dbsession.query(Company).filter(Symbol.name == 'YHOO').first().id)
