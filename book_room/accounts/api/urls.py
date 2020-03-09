from django.conf.urls import url
from django.urls import path, include
from .views import ManagerCreateAPIView, CustomerCreateAPIView

urlpatterns = [
    path('create_manager/',ManagerCreateAPIView.as_view(), name="create_manager"),
    path('create_customer/', CustomerCreateAPIView.as_view(), name="create_customer"),
]
