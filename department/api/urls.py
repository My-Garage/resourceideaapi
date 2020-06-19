from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from department.api.views import DepartmentViewSet

router = DefaultRouter()
router.register('', DepartmentViewSet, 'departments')

urlpatterns = [
    path('departments/', include(router.urls), name='departments'),
]
