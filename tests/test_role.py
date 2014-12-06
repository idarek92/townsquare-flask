
from townsquare.testing import TownSquareTestCase
from townsquare.db import db, Role


class TestRoles(TownSquareTestCase):

    def test_roles_exist(self):
        # the system should set these roles up by default
        self.assertIsNotNone(Role.user())
        self.assertIsNotNone(Role.staff())
        self.assertIsNotNone(Role.admin())
        self.assertIsNotNone(Role.system())

    def test_is_admin_roles(self):
        self.assertFalse(Role.admin().is_user)
        self.assertFalse(Role.admin().is_staff)
        self.assertFalse(Role.admin().is_system)
        self.assertTrue(Role.admin().is_admin)

    def test_is_system_roles(self):
        self.assertFalse(Role.system().is_user)
        self.assertFalse(Role.system().is_staff)
        self.assertTrue(Role.system().is_system)
        self.assertFalse(Role.system().is_admin)

    def test_is_user_roles(self):
        self.assertTrue(Role.user().is_user)
        self.assertFalse(Role.user().is_staff)
        self.assertFalse(Role.user().is_system)
        self.assertFalse(Role.user().is_admin)

    def test_is_staff_roles(self):
        self.assertFalse(Role.staff().is_user)
        self.assertTrue(Role.staff().is_staff)
        self.assertFalse(Role.staff().is_system)
        self.assertFalse(Role.staff().is_admin)








