from rest_framework import serializers
from employee.models import Employee
from organization.api.serializers import OrganizationSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.UUIDField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'file_number', 'phone_number',
                  'phone_number_confirmed', 'status', 'organization',
                  'organization_id', 'user', 'user_id', 'is_resource', )
