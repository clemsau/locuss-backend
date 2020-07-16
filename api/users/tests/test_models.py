from django.test import TestCase

from api.decks.tests.factories import UserFactory


class TestDeckModel(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_deck_str(self):
        """
        Validate the __str__ return of the Deck
        """
        expected = self.user.username
        actual = self.user.__str__()
        self.assertEqual(expected, actual)
