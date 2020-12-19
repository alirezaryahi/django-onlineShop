from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def __str__(self):
        return self.last_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='موضوع')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=200, verbose_name='عنوان کتاب')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    price = models.IntegerField(default=0, verbose_name='قیمت')
    image = models.ImageField(upload_to='books/', null=True, blank=True, verbose_name='تصویر')
    vote = models.IntegerField(default=0)
    is_exist = models.BooleanField(default=True, verbose_name='موجود')
    select = models.CharField(max_length=100, default='book')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'
        ordering = ['-vote']

    def __str__(self):
        return self.title
