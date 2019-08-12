from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from employee.api.views import EmployeeViewSet

router = DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('v0.1/employees/', include(router.urls), name='employees'),
]
