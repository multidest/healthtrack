from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HealthTrackService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^health/', include('Health.urls')),

    url(r'^$', include(admin.site.urls)),
)
