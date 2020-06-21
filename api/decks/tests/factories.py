import factory

from api.users.tests.factories import UserFactory


class DeckFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'decks.Deck'

    id = factory.Faker('uuid4')
    title = factory.Faker('text', max_nb_chars=80)
    description = factory.Faker('text', max_nb_chars=400)
    front_label = factory.Faker('text', max_nb_chars=50)
    back_label = factory.Faker('text', max_nb_chars=50)

    owner = factory.SubFactory(UserFactory)
