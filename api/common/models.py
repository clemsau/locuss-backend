from django.db import models

from api.common.mixins.models import TimestampMixin


class BaseModel(TimestampMixin, models.Model):
    """
    Base model for use throughout the code for any model that needs a timestamp
    """
    class Meta:
        abstract = True
