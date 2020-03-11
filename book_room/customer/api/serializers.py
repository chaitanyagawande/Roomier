from rest_framework.serializers import ModelSerializer, SerializerMethodField
from manager.models import Room, TimeSlot
from rest_framework import status
from customer.models import TimeSlotBook, TimeSlotCancel


class TimeSlotSerializer(ModelSerializer):
    date = SerializerMethodField()

    class Meta:
        model = TimeSlot
        fields = ['id', 'room_id', 'time_slot_owner', 'start_time', 'end_time', 'date']

    def get_date(self, obj):
        date =  self.context['request'].GET["date"]
        return date


class BookTimeSlotSerializer(ModelSerializer):

    class Meta:
        model = TimeSlotBook
        fields = [ 'manager_id', 'date', 'start_time', 'end_time', 'room_id']


class BookSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotBook
        fields = ['customer_id', 'date', 'room_id', 'start_time', 'end_time']


class CancelTimeSlotSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotCancel
        fields = ['manager_id', 'date', 'room_id', 'start_time', 'end_time']