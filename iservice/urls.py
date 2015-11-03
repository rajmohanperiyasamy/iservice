from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD
=======
     # url(r'^blog/', include('blog.urls')),
>>>>>>> c9540690925f5f699bcac2b4454b522a4713b1be


    url(r'^admin/', include(admin.site.urls)),
)  


  #where
