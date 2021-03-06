from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lbtcex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authorize/', include('lbtcex.client.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('lbtcex.main.urls')),
)
