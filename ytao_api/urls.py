from django.conf.urls import url
from django.urls import path, include
from .views import ConverterApiView

urlpatterns = [
    path('api', ConverterApiView),
]
# urlpatterns = [
# ]