from django.contrib import admin
from .models import Book  # relative import, correct way

# Register your models here.

@admin.register(Book)  # decorator style
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown
    list_filter = ('publication_year', 'author')             # filters on right
    search_fields = ('title', 'author')                     # search bar
