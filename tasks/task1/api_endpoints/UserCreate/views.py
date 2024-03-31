from rest_framework.generics import CreateAPIView
from tasks.task1.api_endpoints.UserCreate.serializer import UserCreateSerializer
from tasks.task1.models import User
from rest_framework import status
from rest_framework.response import Response


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        username = serializer.get('username')
        soft_deleted_user = User.objects.filter(username=username, is_deleted=True).first()

        if soft_deleted_user:
            soft_deleted_user.delete()

        serializer.save()
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


__all__ = ('UserCreateView',)
