from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from BatchTagDummyWeb import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BatchTagDummy.views.home', name='home'),
    # url(r'^BatchTagDummy/', include('BatchTagDummy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.view_home_page, name="homepage"),
    url(r'^home$', views.get_home_page, name="homepage"),
    url(r'^furniture$', views.get_furniture_page, name="furniture")

)
