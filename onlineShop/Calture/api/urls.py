from django.urls import path
from .views import AllCalture, UpdateCalture, DeleteCalture, PostCalture

urlpatterns = [
    path('alleffects/', AllCalture.as_view()),
    path('updateeffect/<pk>', UpdateCalture.as_view()),
    path('deleteeffect/<pk>', DeleteCalture.as_view()),
    path('posteffect', PostCalture.as_view()),
]
