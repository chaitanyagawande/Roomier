from django.conf.urls import url
from django.urls import path, include
from .views import RoomListAPIView, RoomDetailAPIView, RoomCreateAPIView, RoomDeleteAPIView, BookTimeSlotAPIView, CancelTimeSlotAPIView, EditAdvanceDayAPIView
from .views import TimeSlotListAPIView, TimeSlotDetailAPIView, TimeSlotDeleteAPIView, TimeSlotUpdateAPIView, TimeSlotCreateAPIView

urlpatterns = [
    path('room/',RoomListAPIView.as_view(), name="list"),
    path('room/create/',RoomCreateAPIView.as_view(), name="create"),
    url(r'^room/(?P<pk>[0-9a-f-]+)/$', TimeSlotListAPIView.as_view(), name="room-detail"),
    url(r'^room/(?P<pk>[0-9a-f-]+)/delete/$', RoomDeleteAPIView.as_view(), name="delete"),
    # Time Slot urls
    url(r'^room/(?P<room_id>[0-9a-f-]+)/slot/create/$',TimeSlotCreateAPIView.as_view(), name="create"),
    url(r'^room/(?P<room_id>[0-9a-f-]+)/slot/(?P<pk>[0-9a-f-]+)/$', TimeSlotDetailAPIView.as_view(), name="timeslot-detail"),
    url(r'^room/(?P<room_id>[0-9a-f-]+)/slot/(?P<pk>[0-9a-f-]+)/edit/$', TimeSlotUpdateAPIView.as_view(), name="timeslot-update"),
    url(r'^room/(?P<room_id>[0-9a-f-]+)/slot/(?P<pk>[0-9a-f-]+)/delete/$', TimeSlotDeleteAPIView.as_view(), name="timeslot-delete"),
    # Booking History urls
    path('bookedtimeslot/', BookTimeSlotAPIView.as_view(), name="booked_time_slot"),
    path('cancelledtimeslot/', CancelTimeSlotAPIView.as_view(), name="cancelled_time_slot"),
    path('edit_advance_days/', EditAdvanceDayAPIView.as_view(), name="edit_advance_days"),
]
