from django.conf.urls import patterns, include, url
from views import submit, new, post_page, voted, register, top_today, top_alltime, top_month, top_year
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PrayList.views.home', name='home'),
    # url(r'^PrayList/', include('PrayList.foo.urls')),
    url(r'^submit/$', submit),
    url(r'^new/$', new),
    url(r'^post/(?P<postid>\d{1,3})/$', post_page),
    (r'^accounts/login/$',  login),
    (r'^/accounts/login/?next=/post/(?P<postid>\d{1,3})/$', login),
    (r'^accounts/logout/$', logout, {'next_page': '/new/'}),
    (r'^voted/(?P<postid>\d{1,3})/$', voted),
    (r'^register/$', register),
    url(r'^top/$', top_today),
    url(r'^top/all$', top_alltime),
    url(r'^top/month$', top_month),
    url(r'^top/year$', top_year),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
