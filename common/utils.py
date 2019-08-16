from django.contrib.auth.models import Group, Permission

from common.permission_lists import administrator_permissions
from common.permission_lists import resource_permissions


def create_resource_groups():
    try:
        resources_group = Group.objects.get(name='organization_resource')
    except Group.DoesNotExist:
        resources_group = Group.objects.create(name='organization_resource')

    resource_permissions_query = Permission.objects\
        .filter(codename__in=resource_permissions)
    resource_permissions_list = (permission
                                 for permission in resource_permissions_query)
    resources_group.permissions.set(resource_permissions_list)


def create_administrator_groups():
    try:
        administrator_group = Group.objects\
            .get(name='organization_administrator')
    except Group.DoesNotExist:
        administrator_group = Group.objects\
            .create(name='organization_administrator')

    admin_permissions_query = Permission.objects\
        .filter(codename__in=administrator_permissions)
    admin_permissions_list = (permission
                              for permission in admin_permissions_query)
    administrator_group.permissions.set(admin_permissions_list)
