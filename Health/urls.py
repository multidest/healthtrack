from django.conf.urls import patterns, url

from Health import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)