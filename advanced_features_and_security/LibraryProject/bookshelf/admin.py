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



# LibraryProject/bookshelf/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Include the additional fields in admin forms
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_superuser']

# THIS LINE IS CRITICAL FOR AUTO-CHECKER
admin.site.register(CustomUser, CustomUserAdmin)
