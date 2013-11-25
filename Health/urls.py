from django.conf.urls import patterns, url

from Health import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<patient_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<patient_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<patient_id>\d+)/vote/$', views.vote, name='vote'),
)