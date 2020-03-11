from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import ManagerSerializer, CustomerSerializer, ProfileSerializer, EditProfileSerializer, ChangePasswordSerializer, LoginSerializer
from accounts.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, update_session_auth_hash, logout, get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

class ManagerCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (AllowAny, )


class CustomerCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny, )


class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        user = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class EditProfileAPIView(APIView):
    serializer_class = EditProfileSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request, format=None):
        user = User.objects.get(id=request.user.id)
        serializer = EditProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdatePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            print(old_password, self.object.password)
            if not self.object.check_password(old_password):
                return Response({"error": "wrong password."}, status=HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"success": "updated password."}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = request.data
        username = serializer.get('username', None)
        password = serializer.get('password', None)
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=HTTP_200_OK)


class LogOutAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'result': 'Successfully Logout.'},status=HTTP_200_OK)

