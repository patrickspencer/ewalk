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
    price = Column(Float)
    # section_name = Column(Integer, ForeignKey(ListingSection.id), nullable=True)

    def __repr__(self):
        return "<QuotePrice(datetime_accessed='%s',price='%s')>" \
                % (self.datetime_accessed, self.price)
    @property
    def serialize(self):
       """
       Return object data in easily serializable format
       """
       return {
           'datetime_accessed': self.datetime_accessed,
           'price': self.price,
       }
