from rest_framework import generics

from employee.permissions import EmployeePermissions
from employee.permissions import RecordOwnerOrAdministrator
from employee.api.serializers import EmployeeSerializer
from employee.models import Employee


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.none()
    serializer_class = EmployeeSerializer
    permission_classes = [EmployeePermissions]

    def get_queryset(self):
        return Employee.objects\
            .filter(
                organization_id=self.request.user.employee.organization_id)\
            .all()

    def perform_create(self, serializer):
        pass


class EmployeeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.none()
    serializer_class = EmployeeSerializer
    permission_classes = [RecordOwnerOrAdministrator]

    def get_queryset(self):
        return Employee.objects\
            .filter(
                organization_id=self.request.user.employee.organization_id)\
            .all()
