from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class CreateUserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


