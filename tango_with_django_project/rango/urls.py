from django.conf.urls import patterns, url
from rango import views

app_name ='rango'

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'), 
        url(r'^about/$', views.about, name='about'),
        #url(r'static$', views.static, name='static')
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!)
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # new!
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'))
        