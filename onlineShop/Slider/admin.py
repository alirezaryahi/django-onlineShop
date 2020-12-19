from django.contrib import admin
from Slider.models import Slider
# Register your models here.



class Slider_admin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Slider


admin.site.register(Slider, Slider_admin)