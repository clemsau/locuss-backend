from rest_framework import viewsets
from .permissions import IsDeckOwnerOrContributor

from api.common.permissions import ReadOnly
from .models import Deck
from .serializers import DeckSerializer


class ListDeckView(viewsets.ModelViewSet):
    permission_classes = [IsDeckOwnerOrContributor | ReadOnly]
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
