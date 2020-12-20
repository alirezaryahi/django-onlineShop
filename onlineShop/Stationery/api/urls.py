from django.urls import path
from .views import AllStationery, UpdateStationery, DeleteStationery, PostStationery

urlpatterns = [
    path('allstationery', AllStationery.as_view()),
    path('updatestationery/<pk>', UpdateStationery.as_view()),
    path('deletestationery/<pk>', DeleteStationery.as_view()),
    path('poststationery', PostStationery.as_view()),
]
