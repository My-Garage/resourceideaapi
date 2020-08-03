import pytest

from task_assignment.models import TaskAssignment
from organization.models import Organization
from employee.models import Employee
from engagement.models import Engagement
from lineofservice.models import LineOfService


@pytest.fixture(scope='function')
def task_assignment(organization: Organization, engagement: Engagement, employee: Employee) -> None:
    return TaskAssignment.objects.create(
        task='Task assignment 1',
        start_date_time='2020-08-03T08:00:00',
        end_date_time='2020-08-03T17:00:00',
        engagement_id=engagement.id,
        employee_id=employee.id,
        status='NOT STARTED',
        organization_id=organization.id)
