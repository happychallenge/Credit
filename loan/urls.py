from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create1/$', views.create1, name='create1'),
    url(r'^create2/$', views.create2, name='create2'),
    url(r'^create3/$', views.create3, name='create3'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^append/$', views.append, name='append'),
]
