from django.conf.urls import url
from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('create_room/', views.RoomCreateView.as_view(), name="create_room"),
    path('booking_history/', views.BookingHistory.as_view(), name="booking_history"),
    path('advance_days/', views.EditAdvanceDays, name="advance_days"),
    url(r'^room/delete/(?P<room_id>\d+)/$', views.RoomDeleteView.as_view(), name='delete_room'),
    url(r'^time-slot/(?P<room_id>\d+)/delete/(?P<slot_id>\d+)/$', views.TimeSlotDeleteView.as_view(), name='delete_slot'),
    url(r'^time-slot/(?P<room_id>\d+)/update/(?P<slot_id>\d+)/$', views.TimeSlotUpdateView, name='update_slot'),
    url(r'^room/(?P<room_id>\d+)/$', views.TimeSlotView.as_view(), name='create_time_slot'),
]
