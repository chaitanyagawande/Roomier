from django.conf.urls import url
from django.urls import path, include
from .views import SearchAPIView, BookTimeSlotAPIView, BookedTimeSlotAPIView, CancelTimeSlotAPIView, CancelledTimeSlotAPIView


urlpatterns = [
    path('search/', SearchAPIView.as_view(), name="search"),
    path('book/', BookTimeSlotAPIView.as_view(), name="book"),
    path('cancel/', CancelTimeSlotAPIView.as_view(), name="cancel"),
    path('booked/', BookedTimeSlotAPIView.as_view(), name="booked_time_slot"),
    path('cancelled/', CancelledTimeSlotAPIView.as_view(), name="cancelled_time_slot"),
]