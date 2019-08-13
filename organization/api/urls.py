from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from organization.api.views import OrganizationViewSet

router = DefaultRouter()
router.register('', OrganizationViewSet)

urlpatterns = [
    path('organizations/', include(router.urls), name='organizations'),
]
