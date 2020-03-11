from rest_framework.serializers import ModelSerializer, CharField, Serializer
from accounts.models import User
from manager.models import AdvanceBooking
from django.contrib.auth.password_validation import validate_password


class ManagerSerializer(ModelSerializer):
    password = CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']
        read_only_field = ('password',)

    def create(self, validated_data):
        user = super(ManagerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        AdvanceBooking.objects.create(manager_id=User.objects.get(id=user.id))
        user.is_manager = True
        user.save()
        return user


class CustomerSerializer(ModelSerializer):
    password = CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']
        read_only_field = ('password',)

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_customer = True
        user.save()
        return user

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

class EditProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'phone']


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        read_only_field = ("password",)
