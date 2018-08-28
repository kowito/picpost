from django.urls import include, path, re_path


from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # url(r'^$', 'picpost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    re_path(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
    re_path(r'^admin/', include(admin.site.urls)),
]

import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
