from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null=False)
