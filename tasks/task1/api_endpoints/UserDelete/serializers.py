from rest_framework.serializers import ModelSerializer
from tasks.task1.models import User


class UserDestroySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')