import pytest


from client.models import Client


@pytest.fixture(scope='function')
def client(organization, client_industry):
    return Client.objects.create(name='Client name 1', address='Address 1', client_industry_id=client_industry.id,  # type: ignore
                                 organization_id=organization.id)
