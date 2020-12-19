from django.urls import path
from .views import book_listview, book_detailview, book_all, bookSearch

urlpatterns = [
    path('books/all', book_all.as_view()),
    path('books/<title>', book_listview.as_view()),
    path('books/<bookid>/<name>', book_detailview),
    path('searchBook=<title>', bookSearch),
]
