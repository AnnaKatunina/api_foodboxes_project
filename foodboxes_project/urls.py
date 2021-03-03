from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from foodboxes_project import settings

apipatterns = [
    path('items/', include('items.urls')),
    path('users/', include('users.urls')),
    path('reviews/', include('reviews.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
