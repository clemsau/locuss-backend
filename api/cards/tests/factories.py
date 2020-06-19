import factory


class CardFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'cards.Card'

    id = factory.Faker('uuid4')
    front_text = factory.Faker('text', max_nb_chars=180)
    back_text = factory.Faker('text', max_nb_chars=180)
