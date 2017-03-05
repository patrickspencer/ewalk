# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~
    Model definitions and class methods
"""

import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.RawConfigParser()
config.read('/etc/okapi_production_settings.ini')
DB_USER = config.get('database', 'DATABASE_USER')
DB_PASS = config.get('database', 'DATABASE_PASSWORD')
DB_NAME = config.get('database', 'DATABASE_NAME')
DB_HOST = config.get('database', 'DATABASE_HOST')
DB_PORT = config.get('database', 'DATABASE_PORT')
DB_URI = 'postgres://%s:%s@%s:%s/%s' % (
         DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

engine = create_engine(DB_URI, echo=False)
Session = sessionmaker(bind=engine)
dbsession = Session()

# from ewalk.models.event import *
# from stubhub.models.listingsnapshot import *
