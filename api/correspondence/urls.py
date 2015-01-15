# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from letters.views import api_root
 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
 
    # Your stuff: custom urls go here
    url(r'^$', api_root),
    url(r'^', include('letters.urls')),
 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
