import factory
from faker import Faker
from faker.providers import lorem  # type: ignore

from organization.tests.factory import OrganizationFactory


faker = Faker()
faker.add_provider(lorem)


class ClientIndustryFactory(factory.django.DjangoModelFactory):
    """Client industry factory"""

    name = faker.word()

    class Meta:
        model = 'client_industry.ClientIndustry'

    organization = factory.RelatedFactory(OrganizationFactory)
