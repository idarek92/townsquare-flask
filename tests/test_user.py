
from townsquare.testing import TownSquareTestCase
from townsquare.db import db, User, Role
from datetime import date


class TestUser(TownSquareTestCase):

    def test_orientation(self):
        u = User()
        # when a user is created, by default he/she
        # hasn't completed orientation
        self.assertFalse(u.completed_orientation)
        self.assertIsNone(u.date_completed_orientation)

    def test_orientation_changes(self):
        u = User()

        # when a user completes orientation we set the right columns
        u.completed_orientation = True
        self.assertEquals(u.date_completed_orientation, date.today())

        u.completed_orientation = False
        self.assertIsNone(u.date_completed_orientation)

    def test_orientation_changes_from_column(self):

        u = User()

        u.date_completed_orientation = date.today()
        self.assertTrue(u.completed_orientation)

    def test_waiver_form(self):

        # the waiver form property behaves just like the orientation one
        u = User()

        self.assertFalse(u.completed_waiver_form)
        self.assertIsNone(u.date_completed_waiver_form)

        # when a user completes orientation we set the right columns
        u.completed_waiver_form = True
        self.assertEquals(u.date_completed_waiver_form, date.today())

        u.completed_waiver_form = False
        self.assertIsNone(u.date_completed_waiver_form)

        u.date_completed_waiver_form = date.today()
        self.assertTrue(u.completed_waiver_form)

    def test_code_of_conduct(self):

        # so does the code of conduct one
        u = User()

        self.assertFalse(u.completed_code_of_conduct)
        self.assertIsNone(u.date_completed_code_of_conduct)

        # when a user completes orientation we set the right columns
        u.completed_code_of_conduct = True
        self.assertEquals(u.date_completed_code_of_conduct, date.today())

        u.completed_code_of_conduct = False
        self.assertIsNone(u.date_completed_code_of_conduct)

        u.date_completed_code_of_conduct = date.today()
        self.assertTrue(u.completed_code_of_conduct)

    def test_default_role(self):
        u = User()
        self.assertEquals(u.role_id, Role.user().id)
