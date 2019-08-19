from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.reverse import reverse

from common.base_test_case import BaseAPITestCase
from employee.models import Employee
from engagement.models import Engagement
from client.models import Client
from lineofservice.models import LineOfService
from client_industry.models import ClientIndustry


class EngagementTestCase(BaseAPITestCase):

    def setUp(self):
        super(EngagementTestCase, self).setUp()
        self.employee = Employee.objects.create(user=self.user,
                                                organization=self.organization,
                                                status='active',
                                                file_number='51251')
        self.client_industry = ClientIndustry.objects.create(
            name='Industry',
            organization=self.organization)
        self.los = LineOfService.objects.create(
            name='Line of service',
            organization=self.organization
        )
        self.engagement_client = Client.objects.create(
            name='Sample client',
            address='Address 1',
            organization=self.organization,
            client_industry=self.client_industry
        )
        self.engagement = Engagement.objects.create(
            organization=self.organization,
            title='Test engagement',
            description='Test enagement description',
            planned_start_date='2019-08-16',
            actual_start_date='2019-08-16',
            planned_end_date='2019-10-16',
            actual_end_date='2019-10-16',
            status='not started')

    def test_list_engagements_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('engagement-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_engagements_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.get(reverse('engagement-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_engagement_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.get(reverse('engagement-detail',
                                           kwargs={'pk': self.engagement.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_engagement_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.get(reverse('engagement-detail',
                                           kwargs={'pk': self.engagement.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_engagement_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.post(reverse('engagement-list'),
                                    {'title': 'Test engagement',
                                     'description': 'Engagement details',
                                     'actual_start_date': '2019-08-19',
                                     'planned_start_date': '2019-08-19',
                                     'planned_end_date': '2019-09-19',
                                     'actual_end_date': '2019-09-19',
                                     'color': '#33300E',
                                     'status': 'not started',
                                     'organization': self.organization,
                                     'manager_id': self.employee.id,
                                     'partner_id': self.employee.id,
                                     'client_id': self.engagement_client.id,
                                     'line_of_service_id': self.los.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_engagement_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.post(reverse('engagement-list'),
                                    {'title': 'Test engagement',
                                     'description': 'Engagement details',
                                     'actual_start_date': '2019-08-19',
                                     'planned_start_date': '2019-08-19',
                                     'planned_end_date': '2019-09-19',
                                     'actual_end_date': '2019-09-19',
                                     'color': '#33300E',
                                     'status': 'not started',
                                     'organization': self.organization,
                                     'manager_id': self.employee.id,
                                     'partner_id': self.employee.id,
                                     'client_id': self.engagement_client.id,
                                     'line_of_service_id': self.los.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_engagement_by_administrator(self):
        org_admin = Group.objects.get(name='organization_administrator')
        self.user.groups.add(org_admin)
        response = self.client.post(reverse('engagement-list'),
                                    {'title': 'Test engagement update',
                                     'description': 'Updated details',
                                     'actual_start_date': '2019-08-19',
                                     'planned_start_date': '2019-08-19',
                                     'planned_end_date': '2019-09-19',
                                     'actual_end_date': '2019-09-19',
                                     'color': '#33300E',
                                     'status': 'not started',
                                     'organization': self.organization,
                                     'manager_id': self.employee.id,
                                     'partner_id': self.employee.id,
                                     'client_id': self.engagement_client.id,
                                     'line_of_service_id': self.los.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_engagement_by_resource(self):
        org_resource = Group.objects.get(name='organization_resource')
        self.user.groups.add(org_resource)
        response = self.client.post(reverse('engagement-list'),
                                    {'title': 'Test engagement update',
                                     'description': 'Updated details',
                                     'actual_start_date': '2019-08-19',
                                     'planned_start_date': '2019-08-19',
                                     'planned_end_date': '2019-09-19',
                                     'actual_end_date': '2019-09-19',
                                     'color': '#33300E',
                                     'status': 'not started',
                                     'organization': self.organization,
                                     'manager_id': self.employee.id,
                                     'partner_id': self.employee.id,
                                     'client_id': self.engagement_client.id,
                                     'line_of_service_id': self.los.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
