from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from task.api.views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path('tasks/', include(router.urls), name='tasks'),
]
