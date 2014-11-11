from django.conf.urls import patterns, url, include
from officespace import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^user/', include('oautherise.urls')),
        url(r'addspaces/$', views.addspace, name="space"),
        )
