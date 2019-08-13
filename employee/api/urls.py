from django.urls import path

from employee.api.views import EmployeeListCreateView
from employee.api.views import EmployeeRetrieveUpdateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('employees/<uuid:pk>/',
         EmployeeRetrieveUpdateView.as_view(),
         name='employee-detail'),
]
