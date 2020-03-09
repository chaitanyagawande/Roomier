from django.test import TestCase
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

    def test_user_creation(self):
        self.assertEquals(self.user1.username, 'Test')
        self.assertEquals(self.user1.is_customer, True)