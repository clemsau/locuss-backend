from rest_framework import viewsets
from .models import Deck
from .serializers import DeckSerializer


class ListDeckView(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
