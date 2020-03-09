from django.contrib import admin

# Register your models here.
from .models import TimeSlotBook, TimeSlotCancel

admin.site.register(TimeSlotBook)
admin.site.register(TimeSlotCancel)