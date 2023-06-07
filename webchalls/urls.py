"""
URL configuration for webchalls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sqli-1/', include('sqli_easy.urls')),
    path('sqli-2/', include('sqli_medium.urls')),
    path('header/', include('header_easy.urls')),
    path('dir/', include('dir.urls')),
    path('starter/', include('starter.urls')),
    path('conundrum/', include('conundrum.urls')),
    path('', include('home.urls')),
    path('traveler/', RedirectView.as_view(url='https://iasad.me/tags/')),

]
