from django.contrib import admin
from . models import Book, Author
# Register your models here.


class AdminBooks(admin.ModelAdmin):
    list_display = ('author','price','qty')
    search_display = ('author','price','qty')


class AdminAuthor(admin.ModelAdmin):
    list_display = ('name',)
    search_display = ('name',)

admin.site.register(Book,AdminBooks)
admin.site.register(Author, AdminAuthor)