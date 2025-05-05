from django.conf import settings
from django.urls import path

from django.contrib import admin

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
]

# serve media
if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
