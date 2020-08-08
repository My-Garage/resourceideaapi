import pytest
from rest_framework.test import APIClient

from employee.models import Employee


@pytest.fixture
def api_client(django_user_model, organization):
    """Fixture to return the APIClient to be used in the tests."""
    client = APIClient()
    user = django_user_model.objects.create(username='superuser@gmail.com', email='superuser@gmail.com',
                                            password='test key', is_superuser=True)
    Employee.objects.create(organization=organization, user=user)  # type: ignore
    client.force_authenticate(user=user)
    return client
