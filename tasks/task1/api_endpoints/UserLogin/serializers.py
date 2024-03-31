from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.response import Response

from rest_framework.serializers import ModelSerializer, CharField
from tasks.task1.models import User


class UserLoginSerializer(ModelSerializer):
    username = CharField(max_length=128)
    password = CharField(max_length=128)

    #
    # if not username or not password:
    #     raise serializers.ValidationError('Username and password are required.')
    #
    # user = authenticate(username=username, password1=password)
    # if not user:
    #     raise serializers.ValidationError('Incorrect username or password.')
    # else:
    #     Response({'token': user.token}, {'message': 'Logged in successfully.'})

    class Meta:
        model = User
        fields = ('username', 'password')
