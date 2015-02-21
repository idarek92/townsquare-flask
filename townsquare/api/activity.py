

from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from townsquare.db import Activity


class ActivityResource(FlaskResource):

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name'
    })

    def list(self, *args, **kwargs):
        return Activity.query.all()
