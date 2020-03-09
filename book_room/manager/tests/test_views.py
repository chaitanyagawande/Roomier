from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from accounts.models import User
from manager.models import Room, TimeSlot


class TestViews(TestCase):

    def setUp(self):
        self.create_room = reverse("manager:create_room")
        self.delete_room = reverse("manager:delete_room", args=[1])
        self.create_time_slot = reverse("manager:create_time_slot", args=[1])
        self.delete_time_slot = reverse("manager:delete_slot", args=[1, 2])

        self.client = Client()
        self.request_factory = RequestFactory()
        self.user1 = User.objects.create_user(
            username='test_user', email='test@gmail.com',
            password='secret_pass', is_manager=True)

    def test_create_room(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_room)
        request.user = self.user1
        self.client.post(self.create_room, {
            'room_owner': request.user,
            'room_name': 'room1'
        })
        room1 = Room.objects.get(id=1)
        self.assertEquals(room1.room_name, 'room1')

    def test_delete_room(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.delete_room)
        request.user = self.user1
        Room.objects.create(room_owner=request.user, room_name='room1')
        Room.objects.get(id=1).delete()
        self.assertEquals(Room.objects.count(), 0)

    def test_create_time_slot(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_time_slot)
        request.user = self.user1
        self.client.post(self.create_room, {
            'room_owner': request.user,
            'room_name': 'room1'
        })
        room1 = Room.objects.get(id=1)
        self.client.post(self.create_time_slot, {
            'time_slot_owner': request.user,
            'room_id': room1,
            'start_time': '03:00:00',
            'end_time': '12:00:00',
        })
        ts = TimeSlot.objects.get(id=1)
        self.assertEquals(ts.room_id.id, 1)

    def test_delete_time_slot(self):
        self.client.login(username="test_user", password="secret_pass")
        request = self.request_factory.get(self.create_time_slot)
        request.user = self.user1
        self.client.post(self.create_room, {
            'room_owner': request.user,
            'room_name': 'room1'
        })
        room1 = Room.objects.get(id=1)
        self.client.post(self.create_time_slot, {
            'time_slot_owner': request.user,
            'room_id': room1,
            'start_time': '03:00:00',
            'end_time': '12:00:00',
        })
        TimeSlot.objects.get(id=1).delete()
        self.assertEquals(TimeSlot.objects.count(), 0)


