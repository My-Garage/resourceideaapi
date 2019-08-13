"""
Permissions for the employee module
"""
from rest_framework import permissions


class EmployeeAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('employee.add_employee'):
            return True

        if request.user.has_perm('employee.change_employee'):
            return True

        return False


class RecordOwnerOrAdministrator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user \
                or (request.user.has_perm('employee.view_employee') and
                    request.user.has_perm('employee.change_employee')):
            return True

        return False
