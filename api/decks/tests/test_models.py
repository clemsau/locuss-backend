from django.test import TestCase

from api.decks.tests.factories import DeckFactory
from api.users.tests.factories import UserFactory


class TestDeckModel(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.deck = DeckFactory(owner=self.user)

    def test_deck_str(self):
        """
        Validate the __str__ return of the Deck
        """
        expected = self.deck.title
        actual = self.deck.__str__()
        self.assertEqual(expected, actual)
