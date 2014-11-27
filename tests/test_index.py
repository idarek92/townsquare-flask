
from townsquare.testing import TownSquareTestCase


class TestHomePage(TownSquareTestCase):

    def test_is_ok(self):
        self.assert200(self.client.get('/'))
