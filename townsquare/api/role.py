
from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from townsquare.db import Role


class RoleResource(FlaskResource):

    preparer = FieldsPreparer({
        'id': 'id',
        'name': 'name'
    })

    def list(self, *args, **kwargs):
        return Role.query.all()
