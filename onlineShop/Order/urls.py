from django.urls import path
from .views import Open_order, add_user_order, remove_order_detail

urlpatterns = [
    path('openOrder', Open_order),
    path('add_user_order', add_user_order),
    path('remove_order_detail/<detail_id>', remove_order_detail),
]
