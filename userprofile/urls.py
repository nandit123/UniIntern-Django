from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from userprofile import views

app_name = 'userprofile'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^profile/add/$', views.ProfileCreate.as_view(), name='profile-add'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^login/$', auth_views.login, {'template_name': 'userprofile/login.html'}),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^studentproject/add/$', views.StudentProjectCreate.as_view(), name='student-project-add'),
    url(r'^studentproject/(?P<pk>[0-9]+)/$', views.StudentProjectUpdate.as_view(), name='student-project-update'),
    url(r'^studentproject/(?P<pk>[0-9]+)/delete/$', views.StudentProjectDelete.as_view(), name='student-project-delete'),
]
