from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    last_update_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Card
        fields = ('created_at',
                  'updated_at',
                  'id',
                  'front_text',
                  'back_text',
                  'deck',
                  'last_update_author',)
