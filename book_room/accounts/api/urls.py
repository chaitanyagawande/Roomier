from django.conf.urls import url
from django.urls import path, include
from .views import ManagerCreateAPIView, CustomerCreateAPIView, login, logout, ProfileAPIView, EditProfileAPIView, UpdatePasswordAPIView, LoginAPIView, LogOutAPIView

urlpatterns = [
    path('create_manager/',ManagerCreateAPIView.as_view(), name="create_manager"),
    path('create_customer/', CustomerCreateAPIView.as_view(), name="create_customer"),
    path('login/', LoginAPIView.as_view(), name="login_api"),
    path('logout/', LogOutAPIView.as_view(), name="logout_api"),
    path('profile/', ProfileAPIView.as_view(), name="profile"),
    path('edit_profile/', EditProfileAPIView.as_view(), name="profile"),
    path('edit_password/', UpdatePasswordAPIView.as_view(), name="edit_password")
]
