import ewalk
from ewalk.models import dbsession
# from ewalk.models.event import Event
# from ewalk.models.listingzone import ListingZone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Float

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    datetime_accessed = Column(DateTime(timezone=True), index=True)
    open = Column(Float)
    low = Column(Float)
    high = Column(Float)
    close = Column(Float)
    adj_close = Column(Float)
    symbol = Column(String)
    volume = Column(Integer)
    # section_name = Column(Integer, ForeignKey(ListingSection.id), nullable=True)

    def __repr__(self):
        return "<QuotePrice( \
                 datetime_accessed='%s', \
                 open='%s', \
                 low='%s', \
                 high='%s', \
                 close='%s', \
                 adj_close='%s', \
                 symbol='%s', \
                 volume='%s' \
                 )>" % (
                 self.datetime_accessed,
                 self.open,
                 self.low,
                 self.high,
                 self.close,
                 self.adj_close,
                 self.symbol,
                 self.volume
                )
    @property
    def serialize(self):
       """
       Return object data in easily serializable format
       """
       return {
           'datetime_accessed': self.datetime_accessed,
           'open': self.open,
           'low': self.low,
           'high': self.high,
           'close': self.close,
           'adj_close': self.adj_close,
           'symbol': self.symbol,
           'volume': self.volume,
       }
