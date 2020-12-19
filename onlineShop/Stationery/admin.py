from django.contrib import admin
from Stationery.models import Group, Stationery


# Register your models here.


class Group_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['title']

    class Meta:
        model = Group


class Stationery_admin(admin.ModelAdmin):
    list_display = ['__str__', 'group']
    search_fields = ['title']
    list_filter = ['group']

    class Meta:
        model = Stationery


admin.site.register(Group, Group_admin)
admin.site.register(Stationery, Stationery_admin)
