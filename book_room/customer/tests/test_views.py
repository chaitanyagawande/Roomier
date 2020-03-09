from datetime import datetime
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from accounts.models import User
from manager.models import Room
from customer.models import TimeSlotBook, TimeSlotCancel
from manager.models import TimeSlot


class TestViews(TestCase):

    def setUp(self):
        self.search_slot = reverse("customer:search")

    def test_search_case(self):
        # GET method
        response = self.client.get(self.search_slot)
        self.assertEquals(response.status_code, 302)
        # POST method
        response = self.client.post(self.search_slot, {
            'start_time': '12:00:00',
            'end_time': '03:00:00',
            'date': datetime.today().date(),
        })
        self.assertEquals(response.status_code, 302)
