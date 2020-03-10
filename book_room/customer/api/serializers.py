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
        # print(date)
        # time_slot_serializer = TimeSlotSerializer()
        return date


class BookTimeSlotSerializer(ModelSerializer):
    #customer_id = SerializerMethodField('get_customer_id')

    class Meta:
        model = TimeSlotBook
        fields = ['customer_id', 'manager_id', 'date', 'start_time', 'end_time', 'room_id']

    def get_customer_id(self, obj):
        customer_id =  self.context['request'].user.pk
        # print(date)
        # time_slot_serializer = TimeSlotSerializer()
        return customer_id


class BookSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotBook
        fields = ['customer_id', 'date', 'room_id', 'start_time', 'end_time']


class CancelTimeSlotSerializer(ModelSerializer):
    class Meta:
        model = TimeSlotCancel
        fields = ['id', 'customer_id','manager_id', 'date', 'room_id', 'start_time', 'end_time']