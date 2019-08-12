from rest_framework import mixins
from rest_framework import viewsets

from employee.api.serializers import EmployeeSerializer
from employee.models import Employee
from common.permissions import IsOrganizationAdministrator


class EmployeeViewSet(mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """Employee view set"""

    queryset = Employee.objects.none()
    serializer_class = EmployeeSerializer
    permission_classes = [IsOrganizationAdministrator, ]

    def get_queryset(self):
        return Employee.objects\
            .filter(
                organization_id=self.request.user.employee.organization_id)\
            .all()
