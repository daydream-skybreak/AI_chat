from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    tokens = models.IntegerField(default=4000)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'username'
    is_anonymous = False
    is_authenticated = True

    class Meta:
        db_table = 'users'


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'chats'
