from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import auth
from . import service
from . import views

app_name = 'bio'
urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^login_auth/$', auth.login_auth, name='login_auth'),
    url(r'^logout_auth/$', auth.logout_auth, name='logout_auth'),
    url(r'^home/$', views.home, name='home'),
    url(r'^server/$', views.server, name='server'),
    url(r'^apps/$', views.apps, name='apps'),
    url(r'^watchdog/$', views.watchdog, name='watchdog'),
    url(r'^receive-logs/$', service.receive_logs, name='receive_logs'),
    url(r'^get-logs/$', service.get_logs, name='get_logs'),
    url(r'^get-server-logs/$', service.get_server_logs, name='get_server_logs')
]

urlpatterns += staticfiles_urlpatterns()
