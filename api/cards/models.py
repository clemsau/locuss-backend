import uuid
from django.db import models

from api.common.models import BaseModel


class Card(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front_text = models.CharField(max_length=180)
    back_text = models.CharField(max_length=180)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.front_text, self.back_text)
