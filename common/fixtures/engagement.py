import pytest

from client.models import Client
from organization.models import Organization


from engagement.models import Engagement


@pytest.fixture(scope='function')
def engagement(organization: Organization, client: Client):
    return Engagement.objects.create(
        title='Engagement 1',
        description='Engagement description',
        client=client.id,
        organization_id=organization.id)
