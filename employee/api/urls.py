from django.urls import path

from employee.api.views import EmployeeCreateView, EmployeeListView
from employee.api.views import EmployeeRetrieveUpdateDeleteView
from employee.api.views import EmployeeTerminateView

urlpatterns = [
    path('employees/add', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<uuid:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
    path('employees/terminate/<uuid:pk>/', EmployeeTerminateView.as_view(), name='employee-terminate'),
]
