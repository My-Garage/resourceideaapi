from uuid import UUID
from typing import NewType

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import generics  # type: ignore
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import status  # type: ignore

from employee.api.serializers import EmployeeCreateSerializer, RetrieveUpdateEmployeeSerializer, TerminateEmployeeSerializer
from employee.models import Employee


OrganizationId = NewType('OrganizationId', UUID)  # OrganizationId type


def _employee_queryset(organization_id: OrganizationId) -> QuerySet:
    """
    Returns the active employees queryset
    """
    return Employee.objects.filter(organization_id=organization_id,  # type: ignore
                                   is_deleted=False,
                                   deleted_at__isnull=True,
                                   date_terminated__isnull=True)


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = EmployeeCreateSerializer

    def get_queryset(self):
        return _employee_queryset(organization_id=self.request.user.employee.organization_id)


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = RetrieveUpdateEmployeeSerializer

    def get_queryset(self):
        queryset = _employee_queryset(organization_id=self.request.user.employee.organization_id)
        view = self.request.query_params.get('view', None)
        if view is not None and view == 'resources':
            queryset = queryset.filter(is_resource=True)

        return queryset


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = RetrieveUpdateEmployeeSerializer

    def get_queryset(self):
        return _employee_queryset(organization_id=self.request.user.employee.organization_id)


class EmployeeTerminateView(APIView):
    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)

        date_terminated = timezone.now().strftime('%Y-%m-%d')
        data = {"date_terminated": date_terminated, "is_deleted": True}
        serializer = TerminateEmployeeSerializer(employee, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesTimelineView(APIView):
    """List the resources timeline dashboard"""
    def get(self, request, format=None):
        pass
