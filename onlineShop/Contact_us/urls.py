from django.urls import path
from .views import contact_us

urlpatterns = [
    path('contactUs', contact_us)
]
