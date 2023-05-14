from django.urls import path
from . import views

urlpatterns = [
path('', views.headar_easy, name='index'),
]