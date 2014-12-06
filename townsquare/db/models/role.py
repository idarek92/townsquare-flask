
from . import db
from sqlalchemy import Column, Integer, Unicode


DEFAULT_ROLES = {
    'system': 'system',
    'admin': 'admin',
    'staff': 'staff',
    'user': 'user',
}



class Role(db.Model):

    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=50), unique=True)

    @staticmethod
    def get_role_by_name(name):
        return Role.query.filter_by(name=DEFAULT_ROLES.get(name)).first()

    @staticmethod
    def admin():
        return Role.get_role_by_name('admin')

    @staticmethod
    def user():
        return Role.get_role_by_name('user')

    @staticmethod
    def staff():
        return Role.get_role_by_name('staff')

    @staticmethod
    def system():
        return Role.get_role_by_name('system')

    @property
    def is_admin(self):
        return self == Role.admin()

    @property
    def is_user(self):
        return self == Role.user()

    @property
    def is_staff(self):
        return self == Role.staff()

    @property
    def is_system(self):
        return self == Role.system()


