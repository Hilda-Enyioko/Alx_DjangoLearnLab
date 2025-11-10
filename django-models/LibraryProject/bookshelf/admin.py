from django.contrib import admin

# Register your models here
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to enable filtering on the right sidebar
    list_filter = ('author', 'publication_year')

    # Fields that are searchable using the search bar
    search_fields = ('title', 'author', 'publication_year')

