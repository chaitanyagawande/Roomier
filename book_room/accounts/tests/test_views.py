from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_manager = reverse("accounts:manager_signup")
        self.create_customer = reverse("accounts:customer_signup")

    def test_create_manager(self):
        # get request
        response = self.client.get(self.create_manager)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/manager_signup_form.html")

        # post request
        response = self.client.post(self.create_manager, {
            'username': 'test',
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '7454454215',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='test').email, 'test@gmail.com')
        self.assertEquals(User.objects.get(username='test').first_name, 'test')

    def test_create_customer(self):
        # get request
        response = self.client.get(self.create_customer)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/customer_signup_form.html")

        # post request
        response = self.client.post(self.create_customer, {
            'username': 'test',
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '7454454215',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='test').email, 'test@gmail.com')
        self.assertEquals(User.objects.get(username='test').first_name, 'test')

    def test_update_profile(self):
        self.update_profile = reverse("accounts:edit_profile")
        self.credentials = {
            'username': 'test',
            'email': 'test@gmail.com',
            'first_name': 'test',
            'last_name': 'test',
            'phone': '7454454215',
        }
        User.objects.create_user(**self.credentials)
        # get request
        response = self.client.get(self.update_profile)
        self.assertEquals(response.status_code, 302)

        # post request
        response = self.client.post(self.update_profile, {
            'username': 'test',
            'email': 'test1@gmail.com',
            'first_name': 'test1',
            'last_name': 'test1',
            'phone': '7454454215',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='test').email, 'test@gmail.com')
        self.assertEquals(User.objects.get(username='test').first_name, 'test')

    def test_login(self):
        self.credentials = {
            'username': 'test',
            'password': 'secret_pass'
        }
        User.objects.create_user(**self.credentials)
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
