# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~
    Model definitions and class methods
"""

import os
import configparser

config = configparser.RawConfigParser()
config.read('/etc/okapi_production_settings.ini')
DB_USER = config.get('database', 'DATABASE_USER')
DB_PASS = config.get('database', 'DATABASE_PASSWORD')
DB_HOST = config.get('database', 'DATABASE_HOST')
DB_PORT = config.get('database', 'DATABASE_PORT')
DB_NAME = config.get('database', 'DATABASE_NAME')
DB_URI = 'postgres://%s:%s@%s:%s/%s' % (
         DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

# BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# DB_URI = "sqlite:///%s" % os.path.join(BASE_PATH,'db.sqlite3')

LOCAL_TIMEZONE = 'US/Eastern'
LOGS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs')

