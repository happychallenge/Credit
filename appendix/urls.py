from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^change/$', views.change, name='change'),
]
