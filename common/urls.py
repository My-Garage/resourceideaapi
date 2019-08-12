from django.urls import path
from django.urls import include

from common.views import index


urlpatterns = [
    path('initialsetup/', index, name='initialsetup'),
]