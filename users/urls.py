from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import SimpleRouter

from users.views import CustomUserCreateViewSet

router = SimpleRouter()

router.register('user/create', CustomUserCreateViewSet, basename='user_creation')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

