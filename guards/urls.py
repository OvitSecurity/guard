from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.guard_list, name='guard_list'),
    url(r'^guard/(?P<pk>\d+)/$', views.guard_detail, name='guard_detail'),
    url(r'^guard/new/$', views.guard_new, name='guard_new'),
    url(r'^guard/(?P<pk>\d+)/edit/$', views.guard_edit, name='guard_edit'),
]
