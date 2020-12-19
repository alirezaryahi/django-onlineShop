from django.contrib import admin
from .models import Order, Order_detail


# Register your models here.


class Order_admin(admin.ModelAdmin):
    list_display = ['owner', 'is_paid', 'payment_date']


admin.site.register(Order, Order_admin)
admin.site.register(Order_detail)
