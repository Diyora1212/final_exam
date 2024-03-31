from rest_framework.generics import DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from tasks.task1.api_endpoints.UserDelete.serializers import UserDestroySerializer
from tasks.task1.models import User


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return Response(data={"message": "User soft deleted. That means user kept in database. Just check."},
                        status=status.HTTP_204_NO_CONTENT)


__all__ = ["UserDestroyView"]
