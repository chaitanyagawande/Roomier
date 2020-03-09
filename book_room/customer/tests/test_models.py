from datetime import datetime
from django.test import TestCase
from customer.models import TimeSlotBook, TimeSlotCancel
from accounts.models import User

from manager.models import Room, TimeSlot


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='Test1',
            first_name='test',
            last_name='test',
            phone='7978797977',
            email='test@gmail.com',
            is_customer=True,
            is_manager=False
        )
        self.user2 = User.objects.create(
            username='Test2',
            first_name='test',
            last_name='test',
            phone='7978797977',
            email='test@gmail.com',
            is_customer=False,
            is_manager=True
        )
        self.room1 = Room.objects.create(
            room_owner=self.user2,
            room_name='chaitanya'
        )
        self.book_slot = TimeSlotBook.objects.create(
            manager_id=self.user2,
            customer_id=self.user1,
            date=datetime.today().date(),
            room_id=self.room1,
            start_time=datetime.strptime('12:00:00', "%H:%M:%S"),
            end_time=datetime.strptime('3:00:00', '%H:%M:%S'),
        )
        self.cancel_slot = TimeSlotCancel.objects.create(
            manager_id=self.user2,
            customer_id=self.user1,
            date=datetime.today().date(),
            room_id=self.room1,
            start_time=datetime.strptime('12:00:00', "%H:%M:%S"),
            end_time=datetime.strptime('3:00:00', '%H:%M:%S'),
        )

    def test_slot_book(self):
        self.assertEquals(self.book_slot.manager_id, self.user2)
        self.assertEquals(self.book_slot.customer_id, self.user1)
        self.assertEquals(self.book_slot.room_id, self.room1)
        self.assertEquals(self.book_slot.date, datetime.today().date())
        self.assertEquals(self.book_slot.start_time, datetime.strptime('12:00:00', "%H:%M:%S"))
        self.assertEquals(self.book_slot.end_time, datetime.strptime('3:00:00', '%H:%M:%S'))

    def test_slot_cancel(self):
        self.assertEquals(self.cancel_slot.manager_id, self.user2)
        self.assertEquals(self.cancel_slot.customer_id, self.user1)
        self.assertEquals(self.cancel_slot.room_id, self.room1)
        self.assertEquals(self.cancel_slot.date, datetime.today().date())
        self.assertEquals(self.cancel_slot.start_time, datetime.strptime('12:00:00', "%H:%M:%S"))
        self.assertEquals(self.cancel_slot.end_time, datetime.strptime('3:00:00', '%H:%M:%S'))