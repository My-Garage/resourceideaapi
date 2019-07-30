from rest_framework import mixins
from rest_framework import viewsets

from engagement.api.serializers import EngagementSerializer
from engagement.models import Engagement


class EngagementViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
