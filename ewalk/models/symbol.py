from sqlalchemy import exists
from ewalk.models import dbsession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Float

Base = declarative_base()


class Symbol(Base):
    __tablename__ = 'symbols'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Symbol( \
                 id='%s', \
                 name='%s', \
                 )>" % (
                 self.id,
                 self.name,
                )

    @staticmethod
    def exists(name):
        """
        Return True if symbol with datetime_accessed exists and False otherwise
        """
        (ret, ), = dbsession.query(exists().where(Symbol.name == name))
        return ret

    @property
    def serialize(self):
       """
       Return object data in easily serializable format
       """
       return {
           'name': self.datetime_accessed,
       }
