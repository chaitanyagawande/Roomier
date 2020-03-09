from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer.views import ProfileView, SearchView, BookView, BookDetailView, CancelView


class TestUrls(SimpleTestCase):

    def test_profile(self):
        url = reverse("customer:profile")
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_search_slot(self):
        url = reverse("customer:search")
        self.assertEquals(resolve(url).func.view_class, SearchView)

    def test_book_slot(self):
        url = reverse("customer:book_slot")
        self.assertEquals(resolve(url).func.view_class, BookView)

    def test_book_detail(self):
        url = reverse("customer:book")
        self.assertEquals(resolve(url).func.view_class, BookDetailView)

    def test_cancel_slot(self):
        url = reverse("customer:cancel")
        self.assertEquals(resolve(url).func.view_class, CancelView)

