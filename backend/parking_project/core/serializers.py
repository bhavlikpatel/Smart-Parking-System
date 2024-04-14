from django.contrib.auth.password_validation import validate_password
from lib import serializers as common_serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from lib import constants

from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop("exclude", None)

        # Adding this next line to the documented example
        read_only_fields = kwargs.pop('read_only_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            existing = set(self.fields)
            for field_name in existing:
                if field_name in exclude:
                    self.fields.pop(field_name)

        # another bit we're adding to documented example, to take care of readonly fields
        if read_only_fields is not None:
            for f in read_only_fields:
                try:
                    self.fields[f].read_only = True
                except KeyError:
                    # not in fields anyway
                    pass


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate_email(self,email):
    #     if email:
    #         seperate_1 = email.split('@')[1]
    #         seperate_2 = seperate_1.split('.')[0]
    #         if not seperate_2 == "gmail":
    #             raise serializers.ValidationError("email should accepted gmail")
    #
    #     return email

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "confirm Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(common_serializers.DynamicFieldsModelSerializer):
    user_type = serializers.SerializerMethodField()

    def get_user_type(self, instance):
        return constants.UserRole.ADMIN if instance.is_superuser else constants.UserRole.NORMAL_USER

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_superuser", "user_type")
        read_only_fields = ("username",)


