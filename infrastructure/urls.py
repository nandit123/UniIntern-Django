from django.conf.urls import url

from . import views

app_name = 'infrastructure'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    url(r'^lab/add/$', views.LabCreate.as_view(), name='lab-add'),
    url(r'^lab/(?P<pk>[0-9]+)/$', views.LabUpdate.as_view(), name='lab-update'),

    url(r'^lab/(?P<pk>[0-9]+)/delete/$', views.LabDelete.as_view(), name='lab-delete'),
]
