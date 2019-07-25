from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from employee.api.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('v0.1/', include(router.urls)),
]
