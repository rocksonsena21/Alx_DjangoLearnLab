from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters on the right-hand side
    list_filter = ('publication_year', 'author')
    
    # Search bar fields
    search_fields = ('title', 'author')

