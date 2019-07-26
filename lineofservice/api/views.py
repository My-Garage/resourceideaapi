from rest_framework import mixins
from rest_framework import viewsets

from lineofservice.api.serializers import LineOfServiceSerializer
from lineofservice.models import LineOfService


class LineOfServiceViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):

    queryset = LineOfService.objects.all()
    serializer_class = LineOfServiceSerializer
