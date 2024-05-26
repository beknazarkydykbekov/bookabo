from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserCreateViewSet(GenericViewSet, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
