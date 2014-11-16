from django.conf.urls import patterns, url, include
from officespace import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^user/', include('oautherise.urls')),
        url(r'addspaces/$', views.addspace, name="addspace"),
        url(r'info/(?P<id>\w+)/$', views.officespaceinfo, name='officespaceinfo'),
        url(r'message/(?P<receiverid>\w+)/$', views.messag, name='messages'),
        url(r'messages/view/$', views.showmessages, name='showmessages'),
        url(r'userprofile/(?P<userprofilename>\w+)/$', views.userprofilename, name='userprofilename'),
        )
