from django.conf.urls import url
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
    url(r'^receive-logs/$', service.receive_logs, name='receive_logs')
]
