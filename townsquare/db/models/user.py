"""
user.py

"""

from . import db
from sqlalchemy import Column, Date, Integer
from datetime import date

class User(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    date_completed_orientation = Column(Date)

    @property
    def completed_orientation(self):
        return self.date_completed_orientation is not None

    @completed_orientation.setter
    def completed_orientation(self, b):
        if b:
            self.date_completed_orientation = date.today()

        else:
            self.date_completed_orientation = None

    date_completed_waiver_form = Column(Date)

    @property
    def completed_waiver_form(self):
        return self.date_completed_waiver_form is not None

    @completed_waiver_form.setter
    def completed_waiver_form(self, b):
        if b:
            self.date_completed_waiver_form = date.today()

        else:
            self.date_completed_waiver_form = None


    date_completed_code_of_conduct = Column(Date)

    @property
    def completed_code_of_conduct(self):
        return self.date_completed_code_of_conduct is not None

    @completed_code_of_conduct.setter
    def completed_code_of_conduct(self, b):
        if b:
            self.date_completed_code_of_conduct = date.today()

        else:
            self.date_completed_code_of_conduct = None




