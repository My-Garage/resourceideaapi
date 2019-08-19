from rest_framework import serializers

from client.api.serializers import ClientSerializer
from employee.api.serializers import ManagerSerializer
from engagement.models import Engagement
from lineofservice.api.serializers import LineOfServiceSerializer
from organization.api.serializers import OrganizationSerializer


class EngagementSerializer(serializers.ModelSerializer):
    """Serializes engagement data"""

    organization = OrganizationSerializer(read_only=True)
    line_of_service = LineOfServiceSerializer(read_only=True)
    line_of_service_id = serializers.UUIDField(write_only=True)
    client_id = serializers.UUIDField(write_only=True)
    client = ClientSerializer(read_only=True)
    manager_id = serializers.UUIDField(write_only=True)
    manager = ManagerSerializer(read_only=True)
    partner = serializers.StringRelatedField(read_only=True)
    partner_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Engagement
        fields = ['id', 'title', 'description', 'planned_start_date',
                  'actual_start_date', 'planned_end_date', 'actual_end_date',
                  'color', 'status', 'manager', 'manager_id', 'partner',
                  'partner_id', 'client', 'client_id', 'line_of_service',
                  'line_of_service_id', 'organization']
