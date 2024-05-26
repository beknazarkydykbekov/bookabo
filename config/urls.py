from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('books.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(), name='redoc'),

]
