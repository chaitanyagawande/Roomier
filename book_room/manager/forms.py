from django.forms import ModelForm

from .models import Room, TimeSlot


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('room_name', )


class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ('start_time', 'end_time',)


class TimeSlotUpdateForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time']