from django.test import TestCase
from manager.forms import RoomForm, TimeSlotForm, TimeSlotUpdateForm


class TestForms(TestCase):

    def test_room_form(self):
        form = RoomForm(data={
            'room_name': 'deluxe',
        })
        self.assertTrue(form.is_valid())

    def test_room_form_no_data(self):
        form = RoomForm(data={})
        self.assertFalse(form.is_valid())

    def test_time_slot_form(self):
        form = TimeSlotForm(data={
            'start_time': '12:00:00',
            'end_time': '3:00:00',
        })
        self.assertTrue(form.is_valid())

    def test_time_slot_form_no_data(self):
        form = TimeSlotForm(data={})
        self.assertFalse(form.is_valid())

    def test_time_slot_form_update(self):
        form = TimeSlotUpdateForm(data={
            'start_time': '12:00:00',
            'end_time': '3:00:00',
        })
        self.assertTrue(form.is_valid())

    def test_time_slot_form_update_no_data(self):
        form = TimeSlotUpdateForm(data={})
        self.assertFalse(form.is_valid())
