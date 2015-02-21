
from restless.preparers import FieldsPreparer

from townsquare.common.rest import TownSquareResource
from townsquare.db import Role


class RoleResource(TownSquareResource):
    model = Role

    preparer = FieldsPreparer({
        'id': 'id',
        'name': 'name'
    })
