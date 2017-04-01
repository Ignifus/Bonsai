from django.conf.urls import url

from . import views

app_name = 'bio'
urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^login_auth/$', views.login_auth, name='home'),
    url(r'^logout_auth/$', views.logout_auth, name='logout_auth'),
    url(r'^home/$', views.home, name='home'),
    url(r'^server/$', views.server, name='server'),
    url(r'^apps/$', views.apps, name='apps'),
]
