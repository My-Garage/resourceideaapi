"""Tests for the client app."""
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.reverse import reverse

from common.base_test_case import BaseAPITestCase
from client.models import Client
from client_industry.models import ClientIndustry
from employee.models import Employee


class ClientTestCase(BaseAPITestCase):

    def setUp(self):
        super(ClientTestCase, self).setUp()
        self.employee = Employee.objects.create(user=self.user,
                                                organization=self.organization,
                                                status='active',
                                                file_number='51251')
        self.client_industry = ClientIndustry.objects.create(
            name='Industry',
            organization=self.organization)
        self.client_obj = Client.objects.create(
            name='Sample client',
            address='Address 1',
            organization=self.organization,
            client_industry=self.client_industry)

    def test_get_clients_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_clients_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_client_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.post(reverse('client-list'),
                                    {'name': 'Test client',
                                     'address': 'Test address',
                                     'organization_id': self.organization.id,
                                     'client_industry_id': self.client_industry.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_client_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.post(reverse('client-list'),
                                    {'name': 'Test client',
                                     'address': 'Test address',
                                     'organization_id': self.organization.id,
                                     'client_industry_id': self.client_industry.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_client_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('client-detail',
                                           kwargs={'pk': self.client_obj.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_client_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.get(reverse('client-detail',
                                           kwargs={'pk': self.client_obj.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.put(reverse('client-detail',
                                           kwargs={'pk': self.client_obj.id}),
                                   {'name': 'Test client',
                                    'address': 'Test address',
                                    'organization_id': self.organization.id,
                                    'client_industry_id': self.client_industry.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.put(reverse('client-detail',
                                           kwargs={'pk': self.client_obj.id}),
                                   {'name': 'Test client',
                                    'address': 'Test address',
                                    'organization_id': self.organization.id,
                                    'client_industry_id': self.client_industry.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
