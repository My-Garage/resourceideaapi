"""
Common permissions.
"""
from rest_framework import permissions


class IsOrganizationResource(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user\
            .groups\
            .filter(name='organization_resource')\
            .exists()


class IsOrganizationAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user\
            .groups\
            .filter(name='organization_administrator')\
            .exists()
