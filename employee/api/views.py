from rest_framework import mixins
from rest_framework import viewsets

from employee.api.serializers import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """Employee view set"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
