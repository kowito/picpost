from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # url(r'^$', 'picpost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
    url(r'^admin/', include(admin.site.urls)),
)

import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        )