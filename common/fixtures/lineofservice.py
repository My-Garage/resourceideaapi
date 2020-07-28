import pytest

from lineofservice.models import LineOfService


@pytest.fixture(scope='function')
def lineofservice(organization):
    return LineOfService.objects.create(name='Line of service 1', organization_id=organization.id)
