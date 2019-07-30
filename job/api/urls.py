from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from job.api.views import JobViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
