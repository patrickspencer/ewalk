from sqlalchemy import exists
from stockwalk.models import dbsession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Float

Base = declarative_base()


class Company(Base):
    __tablename__ = 'stockwalk_companies'

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)
    sector = Column(String)

    def __repr__(self):
        return "<Symbol( \
                 id='%s', \
                 name='%s', \
                 )>" % (
                 self.id,
                 self.symbol,
                 self.name,
                 self.sector,
                )

    @staticmethod
    def exists(name):
        """
        Return True if symbol with datetime_accessed exists and False otherwise
        """
        (ret, ), = dbsession.query(exists().where(Symbol.symbol == symbol))
        return ret

    @property
    def serialize(self):
       """
       Return object data in easily serializable format
       """
       return {
           'symbol': self.symbol,
           'name': self.name,
           'sector': self.sector,
       }
