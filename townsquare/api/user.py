
from restless.preparers import FieldsPreparer

from townsquare.common.rest import TownSquareResource
from townsquare.db import User


class UserResource(TownSquareResource):
    model = User

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'active': 'active',
        'role_id': 'role_id'
    })
