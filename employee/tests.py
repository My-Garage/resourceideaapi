from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse

from common.base_test_case import BaseAPITestCase
from employee.models import Employee


class EmployeeTestCase(BaseAPITestCase):

    def setUp(self):
        super(EmployeeTestCase, self).setUp()
        employee = Employee.objects.create(user=self.user,
                                           organization=self.organization,
                                           status='active',
                                           file_number='51251')
        self.employee_id = employee.id

    def test_list_employees_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('employees'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_employee_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('employee-detail',
                                           kwargs={'pk': self.employee_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['fullname'], 'Serunjogi Joseph')

    def test_employee_update_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.put(
            reverse('employee-detail', kwargs={'pk': self.employee_id}),
            {
                'file_number': '51251',
                'status': 'active',
                'organization_id': self.organization.id,
                'user_id': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_employee_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        user = User.objects.create_user(username='test', password='strongpas')
        response = self.client.post(
            reverse('employees'),
            {
                'file_number': '51252',
                'status': 'active',
                'organization_id': self.organization.id,
                'user_id': user.id
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.get(reverse('employees'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_employee_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        new_user = User.objects.create_user(username='test',
                                            password='strongpas')
        employee = Employee.objects.create(user=new_user,
                                           organization=self.organization,
                                           status='active',
                                           file_number='51253')
        self.user.groups.add(org_resource)
        response = self.client.get(
            reverse('employee-detail', kwargs={'pk': employee.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_employee_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        new_user = User.objects.create_user(username='test',
                                            password='strongpas')
        employee = Employee.objects.create(user=new_user,
                                           organization=self.organization,
                                           status='active',
                                           file_number='51253')
        self.user.groups.add(org_resource)
        response = self.client.put(
            reverse('employee-detail', kwargs={'pk': employee.id}),
            {
                'file_number': '51253',
                'status': 'active',
                'organization_id': self.organization.id,
                'user_id': new_user.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_employee_by_owner(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.put(
            reverse('employee-detail', kwargs={'pk': self.employee_id}),
            {
                'file_number': '51253',
                'status': 'active',
                'organization_id': self.organization.id,
                'user_id': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
