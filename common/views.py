from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.permission_lists import administrator_permissions
from common.permission_lists import resource_permissions


@api_view(['GET'])
def index(request):
    # Add organization resource group permissions.
    try:
        resources_group = Group.objects.get(name='organization_resource')
    except Group.DoesNotExist:
        resources_group = Group.objects.create(name='organization_resource')

    resource_permissions_query = Permission.objects\
        .filter(codename__in=resource_permissions)
    resource_permissions_list = (permission
                                 for permission in resource_permissions_query)
    resources_group.permissions.set(resource_permissions_list)

    # Add organization administrator group permissions.
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

    response = {'message': 'Initial setup complete.'}
    return Response(response)
