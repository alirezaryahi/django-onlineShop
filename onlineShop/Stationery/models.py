from django.db import models


# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Stationery(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='stationeries/', null=True, blank=True, verbose_name='تصویر')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    vote = models.IntegerField(default=0)
    is_exist = models.BooleanField(default=True, verbose_name='موجود')
    select = models.CharField(max_length=100, default='stationery')

    class Meta:
        verbose_name = 'نوشت افزار'
        verbose_name_plural = 'نوشت افزار ها'
        ordering = ['-vote']

    def __str__(self):
        return self.title
