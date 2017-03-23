from django.conf import settings #new import
#from django.conf.urls.static import static #new import
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls', namespace="rango")), # ADD THIS NEW TUPLE!
    )
    

# if settings.DEBUG:
    #urlpatterns += patterns(
        #'django.views.static', 
        #(r'^media/(?P<path>.*)',
       # 'serve',
       # {'document_root': settings.MEDIA_ROOT}), )

#if not settings.DEBUG:
       # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)