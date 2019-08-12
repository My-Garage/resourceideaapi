from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from task_assignment.api.views import TaskAssignmentViewSet


router = DefaultRouter()
router.register('', TaskAssignmentViewSet)

urlpatterns = [
    path('v0.1/taskassignments/', include(router.urls), name='taskassignments'),
]
