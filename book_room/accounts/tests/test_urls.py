from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import CustomerSignUpView, ManagerSignUpView, get_user_profile, UpdateProfile


class TestUrls(SimpleTestCase):

    def test_signup_customer(self):
        url = reverse("accounts:customer_signup")
        self.assertEquals(resolve(url).func.view_class, CustomerSignUpView)

    def test_signup_manager(self):
        url = reverse("accounts:manager_signup")
        self.assertEquals(resolve(url).func.view_class, ManagerSignUpView)

    def test_profile(self):
        url = reverse("accounts:profile")
        self.assertEquals(resolve(url).func, get_user_profile)

    def test_edit_profile(self):
        url = reverse("accounts:edit_profile")
        self.assertEquals(resolve(url).func, UpdateProfile)
