# Django Shell: CRUD Operations on the Book Model

This file documents common Create, Retrieve, Update, and Delete (CRUD) operations executed within a Django shell session using the `bookshelf.models.Book` model.

---

## Setup and Initial State (Retrieve All)

First, we import the model and check the initial state of the database.

```python
>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet []>


## Create: Adding The First Book

>>> book = Book(title='Atomic Habits', author='James Clear', publication_year=2018)
>>> book.save()
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}]>

## Create: Adding Multiple Books via a Loop

>>> book1 = Book(title='The Hitchhiker\'s Guide to the Galaxy', author='Douglas Adams', publication_year=1979)
>>> book2 = Book(title='1984', author='George Orwell', publication_year=1949)
>>> book3 = Book(title='Dune', author='Frank Herbert', publication_year=1965)
>>> book4 = Book(title='Sapiens: A Brief History of Humankind', author='Yuval Noah Harari', publication_year=2014)

>>> book_list = [book1, book2, book3, book4]

# Incorrect loop (IndentationError)
# >>> for x in book_list:
# ... book.save() 
# Traceback (most recent call last): ... IndentationError: expected an indented block

# Correct loop: we call .save() on the loop variable 'x' not the original 'book' variable
>>> for x in book_list:
...     x.save()
... 

# Verify all entries exist (Retrieve)
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}, {'id': 2, 'title': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'publication_year': 1979}, {'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}, {'id': 4, 'title': 'Dune', 'author': 'Frank Herbert', 'publication_year': 00}, {'id': 5, 'title': 'Sapiens: A Brief History of Humankind', 'author': 'Yuval Noah Harari', 'publication_year': 2014}]>

## Retrieve: Accessing a Specific Object
# Incorrect (AttributeError: type object 'Book' has no attribute 'object')
# >>> first_book = Book.object.all()[0]

# Correct
>>> first_book = Book.objects.all()[0]


## Update: Modifying an Existing Record
>>> first_book.publication_year = 2019
>>> first_book.save()
>>> Book.objects.all().values()[0]
{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2019}

# Reverting the change
>>> first_book.publication_year = 2018
>>> first_book.save()
>>> Book.objects.all().values()[0]
{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}


## Delete: Removing a Record
# The index 5 was out of bounds in the interactive session due to zero-based indexing and data changes
# >>> unwanted_book = Book.objects.all()[5] 
# IndexError: list index out of range

# We select the last valid index (index 4 corresponds to ID 5, 'Sapiens')
>>> unwanted_book = Book.objects.all()[4]
>>> unwanted_book.delete()
(1, {'bookshelf.Book': 1})

# Verify the deletion
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}, {'id': 2, 'title': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'publication_year': 1979}, {'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}, {'id': 4, 'title': 'Dune', 'author': 'Frank Herbert', 'publication_year': 1965}]>


