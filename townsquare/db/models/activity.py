from . import db
from sqlalchemy import Column, Integer, Unicode


class Activity(db.Model):
    """
    The Activity class provide access to our
    programs and activities e.g. OpenBuild, OpenHack,
    Community Council, etc.

    """
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(500), unique=True)

    def __init__(self, name):
        self.name = name
