from django.conf.urls import patterns, include, url
from views import submit, new, post_page
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PrayList.views.home', name='home'),
    # url(r'^PrayList/', include('PrayList.foo.urls')),
    url(r'^submit/$', submit),
    url(r'^new/$', new),
    url(r'^post/(?P<postid>\d{1,3})/$', post_page),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
