from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url('', include('vlblog.urls')),
)

# i18n patterns can be only in top-level URLConf
# so non-i18n patterns can't be moved to the app's URLConf
urlpatterns += patterns('vlblog.views',
    url(r'^import/blog/', 'posts.scan'),
    url(r'^import/comments/', 'comments.import_comments'),
)

urlpatterns += patterns('',
    # not possible to customize urls from the comments app?
    url(r'^comments/preview/$', 'threadedcomments.views.preview_comment'),
    url(r'^comments/post/$', 'threadedcomments.views.post_comment'),
    url(r'^comments/', include('django.contrib.comments.urls')),

)
