from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Manage users:
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # Apps
    url(r'^client/', include('client.urls', namespace='client')),
    url(r'^contract/', include('contract.urls', namespace='contract')),
    url(r'^courtier/', include('courtier.urls', namespace='contract')),
    url(r'^app/', include('utilisateur.urls', namespace='app')),
    url(r'^manager/', include('administrateur.urls', namespace='administrateur')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
