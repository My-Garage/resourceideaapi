from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from lineofservice.api.views import LineOfServiceViewSet

router = DefaultRouter()
router.register(r'linesofservice', LineOfServiceViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
