"""
Permissions for the engagement model.
"""
from rest_framework import permissions


class EngagementPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('engagement.add_engagement'):
            return True

        if request.user.has_perm('engagement.change_engagement'):
            return True

        if request.user.has_perm('engagement.view_engagement'):
            return True

        return False
