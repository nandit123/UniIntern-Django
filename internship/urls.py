from django.conf.urls import url
from . import views

app_name = 'internship'

urlpatterns = [
    url(r'^$', views.HomeView, name='home'),

    url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # /internship/company/add
    url(r'^company/add/$', views.CompanyCreate.as_view(), name='company-add'),

    # /internship/company/2/
    url(r'company/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),

    # /internship/company/2/delete
    url(r'^company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),

    # /internship/2/opening/add/
    url(r'^(?P<pk>[0-9]+)/opening/add/$', views.OpeningCreate.as_view(), name='opening-add'),

    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]
