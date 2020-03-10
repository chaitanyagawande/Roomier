from django.db import models
from accounts.models import User
from manager.models import Room
import uuid


class TimeSlotBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manager_id")
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_id")
    date = models.DateField(null=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    class Meta:
        unique_together = ('manager_id', 'date', 'room_id', 'start_time', 'end_time')

    def __str__(self):
        return str(self.date) + "-" + str(self.start_time) + "-" + str(self.end_time)


class TimeSlotCancel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manger_id_cancel")
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_id_cancel")
    date = models.DateField(null=False)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return str(self.date) + "-" + str(self.start_time) + "-" + str(self.end_time)
