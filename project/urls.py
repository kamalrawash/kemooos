from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #english
    url(r'^$', 'main.views.home_eng'),
    url(r'^courses/$', 'main.views.courses'),
    url(r'^imagegallery/$', 'main.views.galary'),
    url(r'^newslist/$', 'main.views.newslist'),
    url(r'^course/(?P<pk>[0-9]+)/$', 'main.views.course'),
    url(r'^register/(?P<pk>[0-9]+)/$', 'main.views.register'),
    url(r'^newsdetails/(?P<pk>[0-9]+)/$', 'main.views.newsdetails'),
    url(r'^aboutus/$','main.views.aboutus'),
    url(r'^courselist/$','main.views.courselist'),
    url(r'^contactus/$','main.views.contactus'),
    url(r'^coursedetailsadmin/(?P<pk>[0-9]+)/$','main.views.courseadmin'),
    url(r'^ourteam/$','main.views.ourteam'),
    url(r'^schedule2018/$','main.views.schedule2018'),


    #arabic
    url(r'^home_ar/$', 'main.views.home_ar'),
    url(r'^courses_ar/$', 'main.views.courses_ar'),
    url(r'^newslist_ar/$', 'main.views.newslist_ar'),
    url(r'^course_ar/(?P<pk>[0-9]+)/$', 'main.views.course_ar'),
    url(r'^register_ar/(?P<pk>[0-9]+)/$', 'main.views.register_ar'),
    url(r'^newsdetails_ar/(?P<pk>[0-9]+)/$', 'main.views.newsdetails_ar'),
    url(r'^aboutus_ar/$','main.views.aboutus_ar'),
    url(r'^courselist_ar/$','main.views.courselist_ar'),
    url(r'^contactus_ar/$','main.views.contactus_ar'),
    url(r'^schedule2018/$','main.views.schedule2018'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)