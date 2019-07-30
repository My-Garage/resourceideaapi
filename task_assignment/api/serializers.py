from rest_framework import serializers
from task.api.serializers import TaskSerializer
from employee.api.serializers import EmployeeSerializer
from task_assignment.models import TaskAssignment


class TaskAssignmentSerializer(serializers.ModelSerializer):
    """Serializer for the TaskAssignment model."""

    task = TaskSerializer(read_only=True)
    task_id = serializers.UUIDField(write_only=True)
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = TaskAssignment
        fields = ('id', 'start_date_time', 'completion_date_time', 'task',
                  'task_id', 'employee', 'employee_id')
