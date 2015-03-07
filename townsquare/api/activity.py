
from restless.preparers import FieldsPreparer

from townsquare.common.rest import TownSquareResource
from townsquare.db import Activity


class ActivityResource(TownSquareResource):
    model = Activity

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name'
    })
