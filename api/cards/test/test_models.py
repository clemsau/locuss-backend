from django.test import TestCase
from fixtureless.factory import create

from api.cards.models import Card


class TestCardModel(TestCase):
    def setUp(self):
        self.card = create(Card)

    def test_card_str(self):
        """
        Validate the str return of the Card
        """
        expected = Card.__str__(self.card)
        actual = self.card.__str__()
        self.assertEqual(expected, actual)
