from rest_framework import serializers
from .models import Deck


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = ('created_at',
                  'updated_at',
                  'id',
                  'title',
                  'description',
                  'front_label',
                  'back_label',
                  'owner',
                  'contributors')
