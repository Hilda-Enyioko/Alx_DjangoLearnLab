from django.db import models

# Create your models here.

"""
Author Model: 
This model represents an author with fields for author_id, name, and email.
An author can have multiple books associated with them.
Each author is uniquely identified by author_id.
"""
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


"""
Book Model:
This model represents a book with fields for book_id, title, publication_year, and a foreign key to the Author model.
Each book is uniquely identified by book_id.
Every book is associated with one author.
If an author is deleted, all their books are also deleted (cascade delete).
The related_name 'books' allows accessing all books of an author via author.books.
"""    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)