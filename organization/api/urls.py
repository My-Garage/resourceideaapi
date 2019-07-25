from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from organization.api.views import OrganizationViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
