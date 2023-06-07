from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usernames/', views.user_view, name='usernames'),
    path('passwords/', views.password_view, name='passwords'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]
