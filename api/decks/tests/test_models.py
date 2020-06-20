from django.test import TestCase

from api.cards.tests.factories import CardFactory


class TestCardModel(TestCase):
    def setUp(self):
        self.card = CardFactory()

    def test_card_str(self):
        """
        Validate the __str__ return of the Card
        """
        expected = '{} - {}'.format(self.card.front_text, self.card.back_text)
        actual = self.card.__str__()
        self.assertEqual(expected, actual)