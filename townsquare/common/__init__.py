"""
Place for helpful functions and classes.

"""


def assertInstance(o, cls, message=None):
    if not isinstance(o, cls):
        if message is None:
            message = 'Invalid instance({}) not instance of {}'.format(o.__class__.__name__, cls.__name__)

        raise TypeError(message)
