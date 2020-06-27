import pytest

from department.models import Department


@pytest.fixture(scope='function')
@pytest.mark.django_db
def department(organization):
    return Department.objects.create(name='Department 1', organization_id=organization.id)
