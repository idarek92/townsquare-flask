
from townsquare.db import TimeEntry
import unittest


class TestTimeEntry(unittest.TestCase):

    def test_creation(self):

        t = TimeEntry()
        # to make it easier for clients when a time entry
        # is created, it's start time is set to when it was
        # initialized, it shouldn't set any end time though
        self.assertIsNotNone(t.start_time)
        self.assertIsNone(t.end_time)




