from rest_framework import serializers
from tasks.task1.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    bio =serializers.CharField(max_length=90)
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio', 'email', 'password1', 'password2')

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("password1 and password2 must match")
        return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            existing_user = User.objects.get(username=value)
            if existing_user.is_deleted:
                return value  # Allow soft-deleted user to be updated
            raise serializers.ValidationError("username already taken")
        return value

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated_data
        password = validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
