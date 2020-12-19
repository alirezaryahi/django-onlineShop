from django.contrib import admin
from .models import Book, Author, Category


# Register your models here.


class Book_admin(admin.ModelAdmin):
    list_display = ['__str__', 'category', 'is_exist']
    search_fields = ['title']
    list_filter = ['is_exist', 'category']

    class Meta:
        model = Book


class Category_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['title']

    class Meta:
        model = Category


class Author_admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['last_name']

    class Meta:
        model = Author


admin.site.register(Book, Book_admin)
admin.site.register(Category, Category_admin)
admin.site.register(Author, Author_admin)
