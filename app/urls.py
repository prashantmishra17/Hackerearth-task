from django.conf.urls import url, include
from .views import Wines

urlpatterns = [
    url(r'wines/', Wines.as_view(), name = 'Wines'),
]