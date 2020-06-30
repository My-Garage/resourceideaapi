import pytest

from department.models import Department


@pytest.fixture(scope='function')
def department(organization):
    return Department.objects.create(name='Department 1', organization_id=organization.id)
