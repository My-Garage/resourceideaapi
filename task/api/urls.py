from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from task.api.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
