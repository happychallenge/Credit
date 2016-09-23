from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bankindex$', views.bankindex, name='bankindex'),
    url(r'^bankcreate/$', views.bankcreate, name='bankcreate'),
    url(r'^creditgradeindex$', views.creditgradeindex, name='creditgradeindex'),
    url(r'^creditgradecreate/$', views.creditgradecreate, name='creditgradecreate'),
]
