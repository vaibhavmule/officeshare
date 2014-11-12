from django.conf.urls import patterns, url, include
from officespace import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^user/', include('oautherise.urls')),
        url(r'addspaces/$', views.addspace, name="addspace"),
        url(r'info/(?P<location>\w+)/$', views.officespaceinfo, name='officespaceinfo'),
        url(r'message/(?P<receiverid>\w+)/$', views.messages, name='messages'),
        url(r'messages/view/$', view.showmessages, name='showmessages'),
        )
