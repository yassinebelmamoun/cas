from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('front.urls', namespace='front')),
    url(r'^client/', include('client.urls', namespace='client')),
    url(r'^contract/', include('contract.urls', namespace='contract')),
]
