from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/customer/', views.CustomerSignUpView.as_view(), name='customer_signup'),
    path('signup/manager/', views.ManagerSignUpView.as_view(), name='manager_signup'),
    path('profile/', views.get_user_profile, name="profile"),
    path('edit_profile/', views.UpdateProfile, name="edit_profile"),
]
