from pytest_factoryboy import register

from client.tests.factory import ClientFactory
from client_industry.tests.factory import ClientIndustryFactory
from organization.tests.factory import OrganizationFactory


pytest_plugins = [
    'common.fixtures.client_industry',
    'common.fixtures.core',
    'common.fixtures.department',
    'common.fixtures.employee',
    'common.fixtures.engagement',
    'common.fixtures.job_position',
    'common.fixtures.lineofservice',
    'common.fixtures.task_assignment',
]

register(ClientFactory, 'client_model')
register(OrganizationFactory, 'organization')
register(ClientIndustryFactory, 'client_industry')
