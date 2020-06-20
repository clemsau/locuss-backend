import factory


class DeckFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'decks.Deck'

    id = factory.Faker('uuid4')
    front_text = factory.Faker('text', max_nb_chars=180)
    back_text = factory.Faker('text', max_nb_chars=180)
