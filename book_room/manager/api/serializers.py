from rest_framework.serializers import ModelSerializer
from manager.models import Room, TimeSlot, AdvanceBooking
from customer.models import TimeSlotBook, TimeSlotCancel

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'url', 'room_name']


class TimeSlotSerializer(ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id' ,'start_time', 'end_time']


class BookSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotBook
        fields = ['customer_id', 'date', 'room_id', 'start_time', 'end_time']


class CancelSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotCancel
        fields = ['customer_id', 'date', 'room_id', 'start_time', 'end_time']


class AdvanceBookingSerializer(ModelSerializer):
    class Meta:
        model = AdvanceBooking
        fields = ('no_of_days', )