from django.conf.urls import url

from dnsQuery import views

urlpatterns = [
    url(r'^', views.index, name='queryList'),
    url(r'^author', views.home),
]
