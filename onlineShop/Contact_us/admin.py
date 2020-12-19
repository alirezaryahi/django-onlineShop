from django.contrib import admin
from Contact_us.models import Contact_us


# Register your models here.


class admin_contact_us(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['title']

    class Meta:
        model = Contact_us


admin.site.register(Contact_us, admin_contact_us)
