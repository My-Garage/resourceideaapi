import pytest
from django.contrib.auth.models import User

from employee.models import Employee


@pytest.fixture(scope='function')
def employee(organization, job_position):
    user_account = User.objects.create(first_name='Test',
                                       last_name='User',
                                       username='testuser',
                                       email='testuser@mail.com',
                                       is_staff=True,
                                       is_active=True)
    return Employee.objects.create(job_position=job_position,
                                   organization=organization,
                                   phone_number='711187734',
                                   file_number='51251',
                                   status='active',
                                   user=user_account,
                                   is_resource=True)
