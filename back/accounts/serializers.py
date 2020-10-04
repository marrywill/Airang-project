from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_auth.models import TokenModel
from rest_auth.utils import import_callable

from .models import Family


User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'child_name',
            'child_gender',
        )


class FamilyDetailSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    class Meta:
        model = Family
        fields = (
            'id',
            'user',
            'name',
            'image',
            'gender'
        )


class UserDetailSerializer(UserUpdateSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        depth = 1
        fields = UserUpdateSerializer.Meta.fields + ('child_image', 'families')


class UserChildImageUpdateSerializer(UserUpdateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'child_image',
        )


class UserFamilySerializer(serializers.ModelSerializer):
    class Meat:
        model = User
        fields = (
            'families'
        )


class FamilyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = (
            'name',
            'image',
            'gender',
        )


class FamilyBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        depth = 1
        fields = (
            'id',
            'name',
            'image',
            'gender',
        )


class FamilyUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    gender = serializers.CharField(required=False)
    class Meta:
        model = Family
        fields = (
            'name',
            'image',
            'gender',
        )


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = TokenModel
        fields = (
            'key',
            'user',
        )


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self, email):
        return email

    def validate_password(self, password):
        return password

    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        user = get_user_model()
        cleaned_data = self.get_cleaned_data()
        user.create_user(**cleaned_data)
        return user