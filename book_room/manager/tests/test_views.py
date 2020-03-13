from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from accounts.models import User
from manager.models import Room, TimeSlot
import uuid
import datetime

class TestViews(TestCase):

    def setUp(self):
        self.create_room = reverse("manager:create_room")
        self.delete_room = reverse("manager:delete_room", args=[uuid.uuid4()])
        # self.delete_time_slot = reverse("manager:delete_slot", args=[1, 2])

        self.client = Client()
        self.request_factory = RequestFactory()
        self.user1 = User.objects.create_user(username='test_user', email='test@gmail.com', password='secret_pass', is_manager=True)
        self.room1 = Room.objects.create(room_owner=self.user1, room_name='room2')
        self.create_time_slot = reverse("manager:create_time_slot", args=[self.room1.id])

    def test_create_room(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_room)
        request.user = self.user1
        self.client.post(self.create_room, {
            'room_owner': request.user,
            'room_name': 'room1'
        })
        room1 = Room.objects.get(room_name="room1")
        self.assertEquals(room1.room_name, 'room1')

    def test_delete_room(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.delete_room)
        request.user = self.user1
        Room.objects.create(room_owner=request.user, room_name='room1')
        Room.objects.get(room_name="room1").delete()
        self.assertEquals(Room.objects.count(), 1) # because we have created one extra room in SetUp method.

    def test_create_time_slot(self, *args, **kwargs):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_time_slot)
        request.user = self.user1
        data = self.client.post(self.create_time_slot, {
            'time_slot_owner': request.user,
            'room_id': self.room1,
            'start_time': '03:00:00',
            'end_time': '06:00:00',
        })
        ts = TimeSlot.objects.get(time_slot_owner=request.user, room_id=self.room1.id)
        self.assertEquals(ts.room_id.id, self.room1.id)
        self.assertEquals(ts.time_slot_owner, request.user)

    def test_delete_time_slot(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_time_slot)
        request.user = self.user1
        data = self.client.post(self.create_time_slot, {
            'time_slot_owner': request.user,
            'room_id': self.room1,
            'start_time': '03:00:00',
            'end_time': '06:00:00',
        })
        ts = TimeSlot.objects.get(time_slot_owner=request.user, room_id=self.room1.id)
        self.assertEquals(ts.room_id.id, self.room1.id)
        self.assertEquals(ts.time_slot_owner, request.user)
        TimeSlot.objects.get(time_slot_owner=request.user, room_id=self.room1.id).delete()
        self.assertEquals(TimeSlot.objects.count(), 0)
        

