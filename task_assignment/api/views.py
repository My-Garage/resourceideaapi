from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from task_assignment.models import TaskAssignment
from task_assignment.api.serializers import TaskAssignmentSerializer


class TaskAssignmentViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """Task assignment view set."""

    queryset = TaskAssignment.objects.all()  # type: ignore
    serializer_class = TaskAssignmentSerializer
