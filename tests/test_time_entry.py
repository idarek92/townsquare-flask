
from townsquare.db import TimeEntry
import unittest
from datetime import datetime, timedelta

# August 1, 2005
D1 = datetime(year=2005, month=8, day=1)

# December 28, 2013
D2 = datetime(year=2013, month=12, day=28)


class TestTimeEntry(unittest.TestCase):

    def test_creation(self):

        t = TimeEntry()
        # to make it easier for clients when a time entry
        # is created, it's start time is set to when it was
        # initialized, it shouldn't set any end time though
        self.assertIsNotNone(t.start_time)
        self.assertIsNone(t.end_time)

    def test_creating_with_times(self):

        n = datetime.utcnow()
        t = TimeEntry(start=n)

        # one should be able to specify the time though
        self.assertEquals(n, t.start_time)
        self.assertIsNone(t.end_time)

        # creating with end time
        t = TimeEntry(end=n)

        self.assertIsNotNone(t.start_time)
        self.assertEquals(n, t.end_time)

    def test_entry_duration(self):

        t = TimeEntry(start=D1, end=D2)
        self.assertEquals(t.duration, timedelta(3071))

    def test_nones(self):
        t = TimeEntry()
        t.duration











