from rest_framework import serializers
from task_assignment.models import TaskAssignment


class TaskAssignmentSerializer(serializers.ModelSerializer):
    """Serializer for the TaskAssignment model."""

    employee_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = TaskAssignment
        fields = ('id', 'start_date_time', 'completion_date_time', 'employee_id')
