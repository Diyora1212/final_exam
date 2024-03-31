from rest_framework_simplejwt.views import TokenObtainPairView
from tasks.task1.serializers import MyTokenObtainPairSerializer
from tasks.task1.models import User


class MyObtainTokenPairView(TokenObtainPairView):
    if User.objects.filter(is_deleted=False).exists():
        serializer_class = MyTokenObtainPairSerializer
