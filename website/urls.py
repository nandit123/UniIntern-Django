from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from internship import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('internship.urls')),
    url(r'^internship/', include('internship.urls')),
    url(r'^infrastructure/', include('infrastructure.urls')),
    url(r'^userprofile/', include('userprofile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)