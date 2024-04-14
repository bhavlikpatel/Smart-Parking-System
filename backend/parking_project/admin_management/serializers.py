from parking_app import models as parking_app_models
from parking_app import constants
from django.contrib.auth.password_validation import validate_password
from lib import serializers as common_serializers
from rest_framework import serializers
from django.utils import timezone
from . import models
from django.contrib.auth.models import User


class PlotSerializer(common_serializers.DynamicFieldsModelSerializer):

    class Meta:
        model = models.Plot
        fields = ("id", "plot_id", "plot_name", "city", "plot_address")


class FixedSlotsSerializer(common_serializers.DynamicFieldsModelSerializer):

    class Meta:
        model = models.Plot
        fields = ("id", "plot_id", "plot_name", "city", "plot_address")


class UserAdminSerializer(common_serializers.DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name', "is_staff", "is_superuser")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "confirm Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=True
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
