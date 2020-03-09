from django.conf.urls import url
from django.urls import path, include
from .views import RoomListAPIView, RoomDetailAPIView, RoomCreateAPIView, RoomDeleteAPIView, BookTimeSlotAPIView, CancelTimeSlotAPIView
from .views import TimeSlotListAPIView, TimeSlotDetailAPIView, TimeSlotDeleteAPIView, TimeSlotUpdateAPIView, TimeSlotCreateAPIView

urlpatterns = [
    path('',RoomListAPIView.as_view(), name="list"),
    path('create/',RoomCreateAPIView.as_view(), name="create"),
    url(r'^room/(?P<pk>\d+)/$', TimeSlotListAPIView.as_view(), name="room-detail"),
    url(r'^(?P<pk>\d+)/delete/$', RoomDeleteAPIView.as_view(), name="delete"),
    # Time Slot urls
    url(r'^room/(?P<room_id>\d+)/slot/create/$',TimeSlotCreateAPIView.as_view(), name="create"),
    url(r'^room/(?P<room_id>\d+)/slot/(?P<pk>\d+)/$', TimeSlotDetailAPIView.as_view(), name="timeslot-detail"),
    url(r'^room/(?P<room_id>\d+)/slot/(?P<pk>\d+)/edit/$', TimeSlotUpdateAPIView.as_view(), name="timeslot-update"),
    url(r'^room/(?P<room_id>\d+)/slot/(?P<pk>\d+)/delete/$', TimeSlotDeleteAPIView.as_view(), name="timeslot-delete"),
    # Booking History urls
    path('bookedtimeslot/', BookTimeSlotAPIView.as_view(), name="booked_time_slot"),
    path('cancelledtimeslot/', CancelTimeSlotAPIView.as_view(), name="cancelled_time_slot"),
]
