from django.urls import path
from . import views

app_name = "customer"


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('book_slot/', views.BookView.as_view(), name="book_slot"),
    path('book/', views.BookDetailView.as_view(), name="book"),
    path('cancel/', views.CancelView.as_view(), name="cancel"),
    path('search_time_slot/', views.SearchTimeSlot, name="search_time_slot")
    ]
