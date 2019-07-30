from rest_framework import serializers
from task.models import Task
from job.api.serializers import JobSerializers


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    job = JobSerializers(read_only=True)
    job_id = serializers.ModelSerializer(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'job', 'job_id')
