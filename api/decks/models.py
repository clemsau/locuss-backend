import uuid
from django.db import models

from api.common.models import BaseModel
from api.users.models import User


class Deck(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=400, blank=True)
    front_label = models.CharField(max_length=50)
    back_label = models.CharField(max_length=50)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    contributors = models.ManyToManyField(
        User,
        through='Contribution',
        through_fields=('deck', 'user'),
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.deck.title)
