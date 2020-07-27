import uuid
from django.db import models

from api.common.models import BaseModel
from api.decks.models import Deck
from api.users.models import User


class Card(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front_text = models.CharField(max_length=180)
    back_text = models.CharField(max_length=180)

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    last_update_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_update_author')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.front_text, self.back_text)
