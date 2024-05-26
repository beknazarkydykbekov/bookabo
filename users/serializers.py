from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'date_joined')

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.password = make_password(password)
        user.save()
        return user
