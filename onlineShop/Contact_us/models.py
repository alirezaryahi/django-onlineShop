from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Contact_us(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشخصه کاربر')
    email = models.EmailField(default='', verbose_name='ایمیل')
    title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    message = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام کاربر'
        verbose_name_plural = 'پیام های کاربران'
