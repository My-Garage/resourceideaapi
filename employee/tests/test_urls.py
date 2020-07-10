from employee.models import Employee
import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from employee.api.serializers import RetrieveUpdateEmployeeSerializer
from job_position.models import JobPosition
from organization.models import Organization


class TestEmployeeEndpoints:
    pytestmark = [pytest.mark.integrationtest, pytest.mark.django_db, ]

    def test_list_employees(self, api_client):
        url = reverse('employee-list')
        resp = api_client.get(url)

        resp_body = resp.json()

        assert resp.status_code == 200
        assert isinstance(resp_body, list)

    def test_add_employee(self, api_client, organization: Organization, job_position: JobPosition):
        url = reverse('employee-create')
        resp = api_client.post(url, {'file_number': '51251',
                                     'organization_id': organization.id,
                                     'phone_number': '0782147101',
                                     'status': 'active',
                                     'first_name': 'Test',
                                     'last_name': 'User',
                                     'username': 'testuser',
                                     'email': 'tuser@mail.com',
                                     'job_position_id': job_position.id,
                                     'is_resource': False}, format='json')

        resp_json = resp.json()

        assert resp.status_code == 201
        assert 'first_name' in resp_json
        assert resp_json['first_name'] == 'Test'
        assert 'last_name' in resp_json
        assert resp_json['last_name'] == 'User'

        user_account = User.objects.filter(username='testuser')[0]
        assert user_account is not None
        assert user_account.get_full_name() == 'Test User'

    def test_retrieve_employee_details(self, api_client, employee: Employee):
        url = reverse('employee-detail', args=[employee.id])
        resp = api_client.get(url)

        resp_body = resp.json()

        assert resp.status_code == 200
        assert 'id' in resp_body

    def test_update_employee(self, api_client, employee: Employee) -> None:
        """
        Test endpoint url that updates an employee detail.
        """
        url = reverse('employee-detail', args=[employee.id])
        employee_data = RetrieveUpdateEmployeeSerializer(employee).data

        assert employee.first_name == employee_data['first_name']

        first_name_before = employee_data['first_name']
        employee_data['first_name'] = 'Changed'

        resp = api_client.put(url, employee_data, format='json')

        employee_query = Employee.objects.get(pk=employee.id)

        assert resp.status_code == 200
        assert first_name_before != employee_data['first_name']
        assert employee_query.first_name == employee_data['first_name']

    def test_delete_employee(self, api_client, employee: Employee) -> None:
        """
        Test deleting an employee
        """
        url = reverse('employee-detail', args=[employee.id])

        assert not employee.is_deleted
        assert employee.deleted_at is None

        resp = api_client.delete(url)

        employee.refresh_from_db()

        assert resp.status_code == 204
        assert employee.is_deleted
        assert employee.deleted_at is not None

    def test_terminate_employee(self, api_client, employee: Employee) -> None:
        """
        Test terminating an employee
        """
        url = reverse('employee-terminate', args=[employee.id])

        assert employee.date_terminated is None
        resp = api_client.patch(url)

        employee.refresh_from_db()

        assert resp.status_code == 200
        assert employee.date_terminated is not None
