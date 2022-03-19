from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.TextField(
        verbose_name='firstname',
        max_length=64,
        default=''
    )
    lastname = models.TextField(
        verbose_name='lastname',
        max_length=64,
        default=''
    )
    birthdate = models.DateField(verbose_name='birth date', default='2000-01-01')
    address = models.TextField(
        verbose_name='address',
        max_length=128,
        default=''
    )

