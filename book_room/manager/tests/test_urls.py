from django.test import SimpleTestCase
from django.urls import reverse, resolve
from manager.views import RoomCreateView, RoomDeleteView, TimeSlotView, TimeSlotUpdateView, TimeSlotDeleteView, BookingHistory, EditAdvanceDays


class TestUrls(SimpleTestCase):

    def test_create_room(self):
        url = reverse("manager:create_room")
        self.assertEquals(resolve(url).func.view_class, RoomCreateView)

    def test_booking_history(self):
        url = reverse("manager:booking_history")
        self.assertEquals(resolve(url).func.view_class, BookingHistory)

    def test_advance_days(self):
        url = reverse("manager:advance_days")
        self.assertEquals(resolve(url).func, EditAdvanceDays)

    def test_delete_room(self):
        url = reverse("manager:delete_room", args=[2])
        self.assertEquals(resolve(url).func.view_class, RoomDeleteView)

    def test_delete_slot(self):
        url = reverse("manager:delete_slot", args=[2,2])
        self.assertEquals(resolve(url).func.view_class, TimeSlotDeleteView)

    def test_update_slot(self):
        url = reverse("manager:update_slot", args=[2, 2])
        self.assertEquals(resolve(url).func, TimeSlotUpdateView)

    def test_create_time_slot(self):
        url = reverse("manager:create_time_slot", args=[2])
        self.assertEquals(resolve(url).func.view_class, TimeSlotView)
