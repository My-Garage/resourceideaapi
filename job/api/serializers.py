from rest_framework import serializers
from engagement.api.serializers import EngagementSerializer
from job.models import Job
from employee.api.serializers import EmployeeSerializer


class JobSerializers(serializers.ModelSerializer):
    """Serializes Job objects"""

    engagement = EngagementSerializer(read_only=True)
    engagement_id = serializers.UUIDField(write_only=True)
    manager = EmployeeSerializer(read_only=True)
    manager_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'planned_start_date', 'status',
                  'actual_start_date', 'planned_end_date', 'actual_end_date',
                  'engagement', 'engagement_id', 'manager', 'manager_id')
