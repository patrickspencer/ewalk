from stockwalk import models
from stockwalk import settings
from sqlalchemy import create_engine, inspect, desc, exists
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DB_URI, echo=True)
session = sessionmaker(bind=engine)
Session = session()

#this next line creates the database if it doesn't exists already
models.Company.metadata.create_all(engine)
models.Quote.metadata.create_all(engine)
