# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~
    Model definitions and class methods
"""

import ewalk
from ewalk import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DB_URI, echo=False)
Session = sessionmaker(bind=engine)
dbsession = Session()

from ewalk.models.quote import *
