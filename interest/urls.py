from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^result/$', views.result, name='result'),
    url(r'^history/$', views.history, name='history'),
]