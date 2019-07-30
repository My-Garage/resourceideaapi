from rest_framework import mixins
from rest_framework import viewsets

from job.api.serializers import JobSerializers
from job.models import Job


class JobViewSet(mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """View sets for the Job app."""

    queryset = Job.objects.all()
    serializer_class = JobSerializers
