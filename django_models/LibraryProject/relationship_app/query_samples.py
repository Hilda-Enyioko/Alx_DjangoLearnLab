import django
import os

# Set the settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author.
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        
        print(f"Book by {author_name}: {[book.title for book in books]}")
    
    except Author.DoesNotExist:
        print(f"This author '{author_name}' does not exist.")

# 2. List all books in a library.
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"This library '{library_name}' does not exist.")

# 3. Retrieve the librarian for a library.
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"This library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"This library '{library_name}' does not have a librarian.")
        
# Example usage
if __name__ == "__main__":
    books_by_author("James Clear")
    books_in_library("Kaizen Library")
    librarian_for_library("Kaizen Library")