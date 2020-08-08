import pytest

from client.models import Client
from organization.models import Organization

from employee.models import Employee
from engagement.models import Engagement
from lineofservice.models import LineOfService


@pytest.fixture(scope='function')
def engagement(
        organization: Organization,
        client: Client,
        employee: Employee,
        lineofservice: LineOfService):
    return Engagement.objects.create(  # type: ignore
        title='Engagement 1',
        description='Engagement description',
        client_id=client.id,
        manager_id=employee.id,
        partner_id=employee.id,
        line_of_service_id=lineofservice.id,
        organization_id=organization.id)
