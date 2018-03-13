from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^create/$', views.create_client, name='create_client'),
    url(r'^list/$', views.list_client, name='list_client'),
    url(r'^detail/(?P<pk>\d+)$', views.detail_client, name='detail_client'),
]
