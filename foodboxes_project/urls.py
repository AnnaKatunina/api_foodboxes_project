from django.contrib import admin
from django.urls import path, include

apipatterns = [
    path('items/', include('items.urls')),
    path('users/', include('users.urls')),
    path('reviews/', include('reviews.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
]
