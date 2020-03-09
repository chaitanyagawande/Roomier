from django.test import TestCase

from accounts.forms import ManagerSignUpForm, UpdateProfileForm, CustomerSignUpForm


class TestForms(TestCase):

    def test_manager_sign_up_form(self):
        form = ManagerSignUpForm(data={
            'username': 'test',
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '8797987979',
            'password1': 'cc600200',
            'password2': 'cc600200'
        })
        self.assertTrue(form.is_valid())

    def test_manager_sign_up_form_no_data(self):
        form = ManagerSignUpForm(data={})
        self.assertFalse(form.is_valid())

    def test_customer_sign_up_form(self):
        form = CustomerSignUpForm(data={
            'username': 'test',
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '8797987979',
            'password1': 'cc600200',
            'password2': 'cc600200'
        })
        self.assertTrue(form.is_valid())

    def test_customer_sign_up_form_no_data(self):
        form = CustomerSignUpForm(data={})
        self.assertFalse(form.is_valid())

    def test_update_profile_form(self):
        form = UpdateProfileForm(data={
            'username': 'test',
            'email': 'test1@gmail.com',
            'first_name': 'test1',
            'last_name': 'test1',
            'phone': '7979879798',
            'password1': 'cc600200',
            'password2': 'cc600200'
        })
        self.assertTrue(form.is_valid())

    def test_update_profile_form_no_data(self):
        form = UpdateProfileForm(data={})
        self.assertFalse(form.is_valid())
