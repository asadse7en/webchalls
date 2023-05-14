from django.urls import path
from . import views

urlpatterns = [
path('', views.sqli_easy, name='index'),
]