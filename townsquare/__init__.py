
from flask import Flask
from flask_cors import CORS


class TownSquare(Flask):

    def init_extension(self, ext, *args, **kwargs):
        """
        Flask extensions follow a pattern where they need to be
        initialized with the application. This method is just an
        alias to ext.init_app(application).

        """
        return ext.init_app(self, *args, **kwargs)

    @staticmethod
    def create_app(config_name=None):

        app = TownSquare(__name__)
        CORS(app, resources={r"/api/*": {"origins": "*"}})

        from .settings import Settings
        app.config.from_object(Settings)

        from townsquare.index import index
        app.register_blueprint(index)

        from townsquare.db import db
        app.init_extension(db)

        from townsquare.api import UserResource
        UserResource.add_url_rules(app, rule_prefix='/api/0.1/users/')

        from townsquare.api import ActivityResource
        ActivityResource.add_url_rules(app, rule_prefix='/api/0.1/activities/')

        from townsquare.api import RoleResource
        RoleResource.add_url_rules(app, rule_prefix='/api/0.1/roles/')

        from townsquare.api import TimeEntryResource
        TimeEntryResource.add_url_rules(app, rule_prefix='/api/0.1/time-entries/')


        return app
