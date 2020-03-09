from rest_framework.serializers import ModelSerializer, CharField
from accounts.models import User

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']
        read_only_field = ('password',)

    def create(self, validated_data):
        user = super(ManagerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
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
