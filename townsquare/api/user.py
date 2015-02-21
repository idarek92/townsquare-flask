
from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from townsquare.db import User


class UserResource(FlaskResource):

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'active': 'active',
        'role_id': 'role_id'
    })

    def list(self, *args, **kwargs):
        return User.query.all()
