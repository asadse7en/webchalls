from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usernames/', views.user_view, name='usernames'),
    path('passwords/', views.password_view, name='passwords'),
]
