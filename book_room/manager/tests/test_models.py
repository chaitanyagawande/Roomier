from datetime import datetime
from django.test import TestCase
from manager.models import Room, TimeSlot, AdvanceBooking
from accounts.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='Test',
            first_name='test',
            last_name='test',
            phone='7978797977',
            email='test@gmail.com',
            is_customer=True,
            is_manager=False
        )
        self.room1 = Room.objects.create(
            room_owner=self.user1,
            room_name='chaitanya'
        )
        self.slot1 = TimeSlot.objects.create(
            room_id=self.room1,
            time_slot_owner=self.user1,
            start_time=datetime.strptime('12:00:00', "%H:%M:%S"),
            end_time=datetime.strptime('3:00:00', '%H:%M:%S'),
        )
        self.advance_book = AdvanceBooking.objects.create(
            manager_id=self.user1,
            no_of_days=10
        )

    def test_room_creation(self):
        self.assertEquals(self.room1.room_owner, self.user1)
        self.assertEquals(self.room1.room_name, 'chaitanya')

    def test_slot_creation(self):
        self.assertEquals(self.slot1.room_id, self.room1)
        self.assertEquals(self.slot1.time_slot_owner, self.user1)
        self.assertEquals(self.slot1.start_time, datetime.strptime('12:00:00', "%H:%M:%S"))
        self.assertEquals(self.slot1.end_time, datetime.strptime('3:00:00', "%H:%M:%S"))

    def test_advance_booking(self):
        self.assertEquals(self.advance_book.manager_id, self.user1)
        self.assertEquals(self.advance_book.no_of_days, 10)


