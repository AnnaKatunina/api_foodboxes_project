from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from foodboxes_project import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Foodboxes project API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

apipatterns = [
    path('items/', include('items.urls')),
    path('carts/', include('carts.urls')),
    path('users/', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
