import factory
from django.contrib.contenttypes.models import ContentType


class DeckFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'decks.Deck'

    id = factory.Faker('uuid4')
    title = factory.Faker('text', max_nb_chars=80)
    description = factory.Faker('text', max_nb_chars=400)
    front_label = factory.Faker('text', max_nb_chars=50)
    back_label = factory.Faker('text', max_nb_chars=50)

    owner = factory.LazyAttribute(lambda o: ContentType.objects.get_for_model(o.content_object))
    contributors = factory.LazyAttribute(lambda o: ContentType.objects.get_for_model(o.content_object))
