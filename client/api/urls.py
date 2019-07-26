from rest_framework.routers import DefaultRouter
from client.api.views import ClientViewSet
from django.urls import path
from django.urls import include


router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
