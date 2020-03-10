from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from accounts import views
from customer.views import IndexPageView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.static import serve
from book_room import settings

urlpatterns = [
    path('', IndexPageView, name="index"),
    path('accounts/password_change/', views.change_password, name="password_change"),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include("accounts.urls")),
    path('manager/', include("manager.urls")),
    path('customer/', include("customer.urls")),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('api/accounts/', include("accounts.api.urls")),
    path('api/manager/', include("manager.api.urls")),
    path('api/customer/', include("customer.api.urls"))
]
