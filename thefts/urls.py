"""thefts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from reports import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^types/(?P<type_slug>[\w-]+)/$', views.typedetail),
    url(r'^types/(?P<type_slug>[\w-]+)/(?P<location_slug>[\w-]+)/$', views.locationtypedetail),
    url(r'^locations/(?P<location_slug>[\w-]+)/$', views.locationdetail),
    url(r'^admin/', admin.site.urls),
]
    
