from django.conf.urls import url
from . import views

app_name = 'administrateur'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^courtier/detail/(?P<pk>\d+)/$', views.courtier_detail, name='courtier_detail'),
    url(r'^courtier/create/$', views.courtier_create, name='courtier_create'),
    url(r'^courtier/create-administrateur/(?P<pk>\d+)$', views.create_courtier_administrateur, name='courtier_create_administrateur'),
    url(r'^courtier/create-administrateur-done/(?P<pk>\d+)$', views.courtier_create_administrateur_done, name='courtier_create_administrateur_done'),
    url(r'^courtier/delete-administrateur/(?P<pk>\d+)$', views.courtier_administrateur_delete, name='courtier_administrateur_delete'),
    url(r'^courtier/update/(?P<pk>\d+)/$', views.courtier_update, name='courtier_update'),
    url(r'^courtier/list/$', views.courtier_list, name='courtier_list'),
    url(r'^courtier/delete/(?P<pk>\d+)/$', views.courtier_delete, name='courtier_delete'),
]
