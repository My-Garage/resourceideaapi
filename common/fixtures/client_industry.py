import pytest


from client_industry.models import ClientIndustry


@pytest.fixture(scope='function')
def client_industry(organization):
    return ClientIndustry.objects.create(name='Client name 1', organization_id=organization.id)
