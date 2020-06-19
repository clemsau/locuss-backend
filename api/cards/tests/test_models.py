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

    def test_card_front_text_max_length(self):
        """
        Validate the max_length of the front_text field
        """
        expected = 180
        actual = self.card._meta.get_field('front_text').max_length
        self.assertEqual(expected, actual)

    def test_card_back_text_max_length(self):
        """
        Validate the max_length of the back_text field
        """
        expected = 180
        actual = self.card._meta.get_field('back_text').max_length
        self.assertEqual(expected, actual)
