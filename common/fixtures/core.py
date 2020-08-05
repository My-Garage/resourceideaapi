from common.fixtures.utils.seed_database import seed_test_db
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from common.enums import Status
from employee.models import Employee
from organization.models import Organization


@pytest.fixture(scope='session')
def organization(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        org = Organization.objects.create(name='Organization 333')
        django_db_blocker.restore()
        return org


@pytest.fixture(scope='session')
def user(organization, django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_superuser(username='joeseggie@gmail.com',
                                             email='jeoseggie@gmail.com',
                                             password='test key',
                                             is_superuser=True)
        Employee.objects.create(user=user, organization=organization, status=Status.ACTIVE.value)
        django_db_blocker.restore()
        return user


@pytest.fixture(scope='session')
def api_client(user):
    """Fixture to return the APIClient to be used in the tests."""
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture(scope='session')
def test_db_seed(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        seed_test_db()
        django_db_blocker.restore()
