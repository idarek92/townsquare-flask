
from townsquare.db.models.role import DEFAULT_ROLES, Role, db


def create_default_roles():

    for _, role_name in DEFAULT_ROLES.items():
        r = Role()
        r.name = role_name
        db.session.add(r)

    db.session.commit()


def bootstrap():

    create_default_roles()




