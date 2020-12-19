from django.contrib import admin
from .models import Effect, Producer, Subject


# Register your models here.


class Effect_admin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'is_exist']
    search_fields = ['title']
    list_filter = ['is_exist', 'subject']

    class Meta:
        model = Effect


class Subject_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['title']

    class Meta:
        model = Subject


class Producer_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['title']

    class Meta:
        model = Producer


admin.site.register(Effect, Effect_admin)
admin.site.register(Subject, Subject_admin)
admin.site.register(Producer, Producer_admin)
