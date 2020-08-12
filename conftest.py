from typing import List
import pytest
from job_position.tests.factory import JobPositionFactory
from department.tests.factory import DepartmentFactory
from pytest_factoryboy import register

from client.tests.factory import ClientFactory
from client_industry.tests.factory import ClientIndustryFactory
from common.tests.factory.user_factory import UserFactory
from employee.tests.factory import EmployeeFactory
from organization.tests.factory import OrganizationFactory
from lineofservice.tests.factory import LineOfServiceFactory
from engagement.tests.factory import EngagementFactory
from task_assignment.tests.factory import TaskAssignmentFactory

pytest_plugins = [
    'common.fixtures.core',
]

register(ClientFactory, 'client')
register(OrganizationFactory, 'organization')
register(ClientIndustryFactory, 'client_industry')
register(EmployeeFactory, 'employee')
register(UserFactory, 'user')
register(DepartmentFactory, 'department')
register(JobPositionFactory, 'job_position')
register(EngagementFactory, 'engagement')
register(LineOfServiceFactory, 'line_of_service')
register(TaskAssignmentFactory, 'task_assignment')


@pytest.fixture
def employees_list(api_client_user):
    fake_employees_list: List = []
    for i in range(5):
        fake_employee = EmployeeFactory(organization=api_client_user.employee.organization)
        if i in [1, 2, 3]:
            fake_employee.is_resource = False
        fake_employee.save()
        fake_employees_list.append(fake_employee)

    return fake_employees_list
