from django.urls import path
from .views import AllBooks, UpdateBooks, DeleteBooks, PostBooks

urlpatterns = [
    path('allbooks', AllBooks.as_view()),
    path('updatebook/<pk>', UpdateBooks.as_view()),
    path('deletebook/<pk>', DeleteBooks.as_view()),
    path('postbook', PostBooks.as_view()),
]
