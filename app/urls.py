from django.conf.urls import url, include
from app import views
from .views import Wines

urlpatterns = [
    url(r'wines/', Wines.as_view(), name = 'Wines'),
    url(r'^$', views.index, name = 'index'),
]