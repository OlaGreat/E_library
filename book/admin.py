from django.contrib import admin
from .models import Book

# Register your models here.

from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'isbn', 'author']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['genre']


@admin.register(models.Author)
class BookAuthor(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_per_page = 10
    search_fields = ['email']


# admin.site.register(models.Book, BookAdmin)
# admin.site.register(models.Book)
# admin.site.register(models.Author)
admin.site.register(models.Address)
admin.site.register(models.BookInstance)
admin.site.register(models.User)
