from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, User


# Create your models here.


class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'شماره تماس'
        verbose_name_plural = 'شماره های تماس'