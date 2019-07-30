from engagement.api.views import EngagementViewSet
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'engagements', EngagementViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
