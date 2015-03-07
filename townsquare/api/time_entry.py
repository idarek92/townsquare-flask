
from restless.preparers import FieldsPreparer

from townsquare.common.rest import TownSquareResource
from townsquare.db import TimeEntry


class TimeEntryResource(TownSquareResource):
    model = TimeEntry

    preparer = FieldsPreparer({
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'activity_id': 'activity_id'
    })

