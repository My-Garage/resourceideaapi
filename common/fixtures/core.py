import pytest
from rest_framework.test import APIClient

from employee.models import Employee


@pytest.fixture
def api_client(api_client_user, organization):
    """Fixture to return the APIClient to be used in the tests."""
    client = APIClient()
    user = api_client_user
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def api_client_user(django_user_model, organization):
    user_account = django_user_model.objects.create(username='superuser@gmail.com', email='superuser@gmail.com',
                                                    password='test key', is_superuser=True)
    Employee.objects.create(organization=organization, user=user_account)  # type: ignore

    return user_account
