from django.conf.urls import url

from . import views

app_name = 'bio'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^server/$', views.server, name='server'),
    url(r'^apps/$', views.apps, name='apps'),
]
