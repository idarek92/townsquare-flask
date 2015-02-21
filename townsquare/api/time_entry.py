
from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from townsquare.db import TimeEntry


class TimeEntryResource(FlaskResource):

    preparer = FieldsPreparer({
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'activity_id': 'activity_id'
    })

