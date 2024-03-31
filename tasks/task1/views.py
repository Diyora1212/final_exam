from django.contrib.auth import authenticate
# views.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
# from rest_framework.request import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from tasks.task1.serializers import MyTokenObtainPairSerializer
from tasks.task1.models import User


class MyObtainTokenPairView(TokenObtainPairView):
    if User.objects.filter(is_deleted=False).exists():
        serializer_class = MyTokenObtainPairSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     username = serializer.validated_data.get('username')
    #     password = serializer.validated_data.get('password')
    #
    #     # Authenticate user
    #     user = authenticate(request, username=username, password=password)
    #
    #     if user is None:
    #         raise AuthenticationFailed(_('Invalid username or password.'))
    #
    #     # Check if the user is soft-deleted
    #     if user.is_deleted:
    #         raise AuthenticationFailed(_('Your account has been deleted.'))
    #
    #     # Check if the user is active
    #     if not user.is_active:
    #         raise AuthenticationFailed(_('Your account is inactive.'))
    #
    #     # Generate tokens if authentication succeeds
    #     refresh = RefreshToken.for_user(user)
    #     return Response({
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     })
