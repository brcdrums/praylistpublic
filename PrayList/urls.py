from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PrayList.views.home', name='home'),
    # url(r'^PrayList/', include('PrayList.foo.urls')),
    url(r'^submit/$', views.submit),
    url(r'^submit/group/(?P<group_name>.+)/$', views.submit),
    url(r'^submitgroup/$', views.submit_group),
    url(r'^submitgroup/(?P<groupname>.+)/success/$', views.submit_group_success),
    url(r'^new/$', views.new),
    url(r'^post/(?P<postid>\d{1,3})/$', views.post_page),
    url(r'^group/(?P<group>.+)/trending/$', views.groups),
    url(r'^group/(?P<group>.+)/new/$', views.groups_new),
    url(r'^new/?count=(?P<count>\d{1,3})/$', views.new),
    url(r'^/?count=(?P<count>\d{1,3})/$', views.trending),
    url(r'^group/(?P<group>.+)/top/today/$', views.groups_top_today),
    url(r'^group/(?P<group>.+)/top/week/$', views.groups_top_week),
    url(r'^group/(?P<group>.+)/top/month/$', views.groups_top_month),
    url(r'^group/(?P<group>.+)/top/year/$', views.groups_top_year),
    url(r'^group/(?P<group>.+)/top/all/$', views.groups_top_all),
    url(r'^group/(?P<group>.+)/top/today/?count=(?P<count>\d{1,3})/$', views.groups_top_today),
    url(r'^group/(?P<group>.+)/top/week/?count=(?P<count>\d{1,3})/$', views.groups_top_week),  
    url(r'^group/(?P<group>.+)/top/month/?count=(?P<count>\d{1,3})/$', views.groups_top_month),
    url(r'^group/(?P<group>.+)/top/year/?count=(?P<count>\d{1,3})/$', views.groups_top_year),
    url(r'^group/(?P<group>.+)/top/all/?count=(?P<count>\d{1,3})/$', views.groups_top_all),   
    (r'^accounts/login/$', login),
    (r'^/accounts/login/?next=/post/(?P<postid>\d{1,3})/$', login),
    (r'^/accounts/login/?next=/submit/$', login),
    (r'^/accounts/login/?next=/submitgroup/$', login),
    (r'^accounts/logout/$', views.logout_view),
    (r'^voted/(?P<postid>\d{1,3})/$', views.voted),
    (r'^register/$', views.register),
    url(r'^top/$', views.top_today),
    url(r'^top/all/$', views.top_alltime),
    url(r'^top/month/$', views.top_month),
    url(r'^top/year/$', views.top_year),
    url(r'^top/week/$', views.top_week),
    url(r'^top/?count=(?P<count>\d{1,3})/$', views.top_today),
    url(r'^top/all/?count=(?P<count>\d{1,3})/$', views.top_alltime),
    url(r'^top/month/?count=(?P<count>\d{1,3})/$', views.top_month),
    url(r'^top/year/?count=(?P<count>\d{1,3})/$', views.top_year),
    url(r'^top/week/?count=(?P<count>\d{1,3})/$', views.top_week),
    url(r'^$', views.trending),
    url(r'^managegroups/$', views.managegroups),
    url(r'^managegroups/(?P<groupid>\d{1,3})/$', views.managegroups),
    url(r'^managegroups/(?P<groupid>\d{1,3})/unsubscribe/$', views.managegroups),
    url(r'^mypraylist/$', views.my_praylist),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
