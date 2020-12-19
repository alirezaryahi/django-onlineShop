from django.db import models


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'

    def __str__(self):
        return self.title


class Producer(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام')

    class Meta:
        verbose_name = 'تولید کننده'
        verbose_name_plural = 'تولید کنندگان'

    def __str__(self):
        return self.title


class Effect(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='موضوع')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='تولید کننده')
    title = models.CharField(max_length=200, verbose_name='عنوان اثر')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    price = models.IntegerField(default=0, verbose_name='قیمت')
    image = models.ImageField(upload_to='effect/', null=True, blank=True, verbose_name='تصویر')
    vote = models.IntegerField(default=0)
    is_exist = models.BooleanField(default=True, verbose_name='موجود')
    select = models.CharField(max_length=100, default='effect')

    class Meta:
        verbose_name = 'اثر'
        verbose_name_plural = 'آثار'
        ordering = ['-vote']

    def __str__(self):
        return self.title
