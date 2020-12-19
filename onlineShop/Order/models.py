from django.contrib.auth.models import User
from django.db import models
from Calture.models import Effect
from Library.models import Book
from Stationery.models import Stationery


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='زمان پرداخت')

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def get_total_price(self):
        total = 0
        for detail in self.order_detail_set.all():
            if detail.book:
                total += detail.book.price
            if detail.effect:
                total += detail.effect.price
            if detail.stationery:
                total += detail.stationery.price
        return total


class Order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='مشخصه سفارش')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    effect = models.ForeignKey(Effect, on_delete=models.CASCADE, blank=True, null=True)
    stationery = models.ForeignKey(Stationery, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'
