from django.db import models
import uuid
from accounts.models import User


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=10, null=False)

    class Meta:
        unique_together = ('room_owner', 'room_name')

    def __str__(self):
        return self.room_name

    def __unicode__(self):
        pass


class TimeSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_slot_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    class Meta:
        unique_together = ('room_id', 'start_time', 'end_time')

    def __str__(self):
        return str(self.start_time) + "-" + str(self.end_time)


class AdvanceBooking(models.Model):
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_manager_id")
    no_of_days = models.IntegerField(null=False, default=15, blank=False)

    def __str__(self):
        return str(self.manager_id) + " " + str(self.no_of_days)