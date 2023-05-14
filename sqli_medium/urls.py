from django.urls import path
from . import views

urlpatterns = [
path('', views.sqli_medium, name='index'),
]