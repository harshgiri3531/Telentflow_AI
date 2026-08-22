from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from apps.notifications.models import Notification


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'role', 'phone_number',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            role=User.Role.EMPLOYEE,
        )
        Notification.objects.create(
            recipient=user,
            message=f"Welcome to TalentFlow AI, {user.first_name or user.username}! Your account has been created successfully."
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone_number', 'is_active_employee',
        )
        read_only_fields = ('id', 'role')