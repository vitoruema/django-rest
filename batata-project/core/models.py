from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class RegrEntry(object):
    def __init__(self, **kwargs):
        for field in ('type', 'length', 'ini_velo', 'route'):
            setattr(self, field, kwargs.get(field, None))
