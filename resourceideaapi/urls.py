"""resourceideaapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path


BASE_API_URL = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{BASE_API_URL}', include('organization.api.urls')),
    path(f'{BASE_API_URL}', include('employee.api.urls')),
    path(f'{BASE_API_URL}', include('client_industry.api.urls')),
    path(f'{BASE_API_URL}', include('client.api.urls')),
    path(f'{BASE_API_URL}', include('lineofservice.api.urls')),
    path(f'{BASE_API_URL}', include('engagement.api.urls')),
    path(f'{BASE_API_URL}', include('job.api.urls')),
    path(f'{BASE_API_URL}', include('task.api.urls')),
    path(f'{BASE_API_URL}', include('task_assignment.api.urls')),
]
