
from . import db
from sqlalchemy import Column, Integer, Unicode


class Location(db.Model):
    """
    Locations where our events take place in.

    """
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100))
    address = Column(Unicode(100))
    city = Column(Unicode(100))
    state = Column(Unicode(2))
    zip = Column(Unicode(12))
