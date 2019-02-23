from rest_framework import serializers
from apps.authentication.clouds import BaseAuthSerializer
from apps.authentication.models import User
import apps.authentication.exceptions as exceptions


class EmailSignUpSerializer(BaseAuthSerializer):
    auth_cloud_client_handler = 'create_user_with_email_and_password'
    auth_fail_error_class = exceptions.EmailExistsError

    def create_or_get_django_user_from_cloud_user(self, user):
        # TODO: Create django user.
        return user


class EmailLoginSerializer(BaseAuthSerializer):
    auth_cloud_client_handler = 'sign_in_with_email_and_password'
    auth_fail_error_class = exceptions.WrongEmailOrPasswordError

    def create_or_get_django_user_from_cloud_user(self, user):
        # TODO: Get django user.
        return user


class UserSerializer(serializers.Serializer):
    auth_fail_error_class =exceptions.UserExceptions.UserNotFound
    first_name = serializers.CharField(max_length= 30)
    last_name = serializers.CharField(max_length= 30)
    phone = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        return instance
