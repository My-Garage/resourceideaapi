import pytest

from job_position.models import JobPosition


@pytest.fixture(scope='function')
def job_position(organization, department):
    return JobPosition.objects.create(title='Job position 1',  # type: ignore
                                      hierarchy_order=99,
                                      department_id=department.id,
                                      organization_id=organization.id)
