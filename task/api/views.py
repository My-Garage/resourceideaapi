from rest_framework import mixins
from rest_framework import viewsets
from task.models import Task
from task.api.serializers import TaskSerializer


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """Task app view set."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
