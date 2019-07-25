from rest_framework import serializers
from employee.models import Employee
from organization.api.serializers import OrganizationSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    organization = OrganizationSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Employee
        exclude = ('created_at', 'updated_at', )
