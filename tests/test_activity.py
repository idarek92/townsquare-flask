
from townsquare.db import Activity
from townsquare.testing import TownSquareTestCase


class TestActivity(TownSquareTestCase):

    def test_activity_name(self):
        a = Activity('Open Build')
        self.assertEquals(a.name, 'Open Build')
