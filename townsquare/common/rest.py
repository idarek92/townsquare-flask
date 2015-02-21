"""

"""

from restless.fl import FlaskResource


class TownSquareResource(FlaskResource):

    model = None

    def list(self, *args, **kwargs):
        return self.model.query.all()

    def detail(self, pk):
        return self.model.query.get(pk)


