from django.conf.urls import include, url
from django.contrib import admin

from reports import views

#THIS IS THE WRONG URLS FILE

urlpatterns = [
    url(r'^$', views.index), 

    url(r'^/types/(?P<type_slug>[\w-]+)/$', views.typedetail),
   
    url(r'^admin/', admin.site.urls),
]

