from django.conf.urls import patterns, include, url
from views import submit, new, post_page, voted, register, top_today, top_alltime, top_month, top_year, top_week, trending, tags, tags_new, tags_top_today, tags_top_week, tags_top_month, tags_top_year, tags_top_all, submit_group, submit_group_success
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PrayList.views.home', name='home'),
    # url(r'^PrayList/', include('PrayList.foo.urls')),
    url(r'^submit/$', submit),
    url(r'^submit/group/(?P<groupname>.+)/$', submit),
    url(r'^submitgroup/$', submit_group),
    url(r'^submitgroup/(?P<groupname>.+)/success/$', submit_group_success),
    url(r'^new/$', new),
    url(r'^post/(?P<postid>\d{1,3})/$', post_page),
    url(r'^group/(?P<tags>.+)/trending/$', tags),
    url(r'^group/(?P<tags>.+)/new/$', tags_new),
    url(r'^group/(?P<tags>.+)/top/today/$', tags_top_today),
    url(r'^group/(?P<tags>.+)/top/week/$', tags_top_week),
    url(r'^group/(?P<tags>.+)/top/month/$', tags_top_month),
    url(r'^group/(?P<tags>.+)/top/year/$', tags_top_year),
    url(r'^group/(?P<tags>.+)/top/all/$', tags_top_all),           
    (r'^accounts/login/$',  login),
    (r'^/accounts/login/?next=/post/(?P<postid>\d{1,3})/$', login),
    (r'^accounts/logout/$', logout, {'next_page': '/new/'}),
    (r'^voted/(?P<postid>\d{1,3})/$', voted),
    (r'^register/$', register),
    url(r'^top/$', top_today),
    url(r'^top/all/$', top_alltime),
    url(r'^top/month/$', top_month),
    url(r'^top/year/$', top_year),
    url(r'^top/week/$', top_week),
    url(r'^$', trending),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
