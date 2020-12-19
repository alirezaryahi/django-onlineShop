from django.db import models


# Create your models here.


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/', null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
