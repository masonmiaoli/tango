from django.conf.urls import patterns, url
import views 


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^display/(\d+)', views.display, name='display'),

    url(r'^.+', views.missing, name='missing'),
)