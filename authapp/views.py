from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from authapp.serializers import CreateUserModelSerializer


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserModelSerializer
