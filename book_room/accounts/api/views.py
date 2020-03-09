from rest_framework.generics import CreateAPIView
from .serializers import ManagerSerializer, CustomerSerializer
from accounts.models import User
from rest_framework.permissions import AllowAny

class ManagerCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (AllowAny, )


class CustomerCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny, )