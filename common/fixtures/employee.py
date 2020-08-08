from typing import List
from organization.models import Organization
from job_position.models import JobPosition
import pytest
from django.contrib.auth.models import User

from employee.models import Employee


def _create_user(email: str, username: str, **kwargs) -> User:
    """Utility function to create a user"""
    return User.objects.create(first_name=kwargs.get('first_name', 'Test'),
                               last_name=kwargs.get('last_name', 'User'),
                               username=username,
                               email=email,
                               is_staff=kwargs.get('is_staff', True),
                               is_active=kwargs.get('is_active', True))


def _create_employee(phone_number: str, file_number: str, **kwargs) -> Employee:
    """Utility function to create an employee"""
    return Employee.objects.create(job_position_id=kwargs.get('job_position_id', None),  # type: ignore
                                   organization_id=kwargs.get('organization_id', None),
                                   phone_number=phone_number,
                                   file_number=file_number,
                                   status=kwargs.get('status', 'ACTIVE'),
                                   user_id=kwargs.get('user_account_id', None),
                                   is_resource=kwargs.get('is_resource', False))


@pytest.fixture(scope='function')
def employee(organization: Organization, job_position: JobPosition):
    user_account = _create_user(email='test@mail.com', username='testuser')
    return _create_employee(job_position_id=job_position.id, organization_id=organization.id, file_number='51251',
                            user_account_id=user_account.id, phone_number='711187734', status='ACTIVE')  # type: ignore


@pytest.fixture(scope='function')
def employee_list(organization, job_position) -> List[Employee]:
    employee_dir: list = []

    user_account_1: User = _create_user(email='test+user1@mail.com', username='testuser1')
    user_account_2: User = _create_user(email='test+user2@mail.com', username='testuser2')
    employee_dir.append(_create_employee(job_position_id=job_position.id, organization_id=organization.id,
                                         file_number='51252', user_account_id=user_account_1.id,  # type: ignore
                                         phone_number='711134544', status='ACTIVE', is_resource=True))
    employee_dir.append(_create_employee(job_position_id=job_position.id, organization_id=organization.id,
                                         file_number='51253', user_account_id=user_account_2.id,  # type: ignore
                                         phone_number='711134534', status='ACTIVE', is_resource=True))

    return employee_dir
