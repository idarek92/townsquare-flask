"""
user.py

"""

from . import db
from sqlalchemy import Column, Date, Integer, UnicodeText, Unicode, Boolean
from datetime import date
from .role import Role


class User(db.Model):
    """
    A user as it stands on our system.

    For some details see:
    https://github.com/sc3/townsquare-flask/issues/3

    The 3 date_completed_* columns have to do with how
    FreeGeek Chicago works. New volunteers need to go
    through a orientation. They need to sign a waiver form
    and agree to our code of conduct.

    http://freegeekchicago.org/volunteer

    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(500), unique=True)

    date_completed_orientation = Column(Date)
    date_completed_waiver_form = Column(Date)
    date_completed_code_of_conduct = Column(Date)

    emergency_contact = Column(UnicodeText(length=300))

    first_name = Column(Unicode(100))
    last_name = Column(Unicode(100))

    active = Column(Boolean, default=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, role_id=None):

        if role_id is None:
            role_id = Role.user().id

        self.role_id = role_id

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def completed_orientation(self):
        return self.date_completed_orientation is not None

    @completed_orientation.setter
    def completed_orientation(self, b):
        if b:
            self.date_completed_orientation = date.today()

        else:
            self.date_completed_orientation = None

    @property
    def completed_waiver_form(self):
        return self.date_completed_waiver_form is not None

    @completed_waiver_form.setter
    def completed_waiver_form(self, b):
        if b:
            self.date_completed_waiver_form = date.today()

        else:
            self.date_completed_waiver_form = None

    @property
    def completed_code_of_conduct(self):
        return self.date_completed_code_of_conduct is not None

    @completed_code_of_conduct.setter
    def completed_code_of_conduct(self, b):
        if b:
            self.date_completed_code_of_conduct = date.today()

        else:
            self.date_completed_code_of_conduct = None
