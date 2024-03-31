from rest_framework.exceptions import APIException
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_deleted is True:
            raise APIException("User have been deleted softly that means can register again by same data.")
        token = super().get_token(user)
        return token
