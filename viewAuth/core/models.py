from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


class User(AbstractUser):
    department = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)
    USER_TYPE_CHOICES = (
        (1, 'client'),
        (2, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=1)

    class meta:
        pass


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=CASCADE, default=1, unique=True)
    description = models.CharField(max_length=50)


class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=CASCADE, default=1, unique=True)
    other = models.CharField(max_length=50)
