from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^hit', views.hit, name='hit'),
    url(r'^list', views.list, name='list')
)