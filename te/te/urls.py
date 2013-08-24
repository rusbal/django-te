from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.home_page', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
