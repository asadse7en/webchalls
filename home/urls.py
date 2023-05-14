from django.urls import path
from .views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    # Add URL patterns for your sub-apps here
]