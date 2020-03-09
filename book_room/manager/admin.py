from django.contrib import admin

# Register your models here.
from .models import Room, TimeSlot, AdvanceBooking

admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(AdvanceBooking)