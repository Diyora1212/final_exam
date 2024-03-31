from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


class AbstractModel(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = CharField(max_length=30, unique=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        super().delete(*args, **kwargs)
