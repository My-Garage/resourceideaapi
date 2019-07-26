from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from client.api.views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
