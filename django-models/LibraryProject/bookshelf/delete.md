# Delete: Removing a Record

>>> from bookshelf.models import Book
>>> """
>>> The index 5 was out of bounds in the interactive session due to zero-based indexing and data changes
>>> unwanted_book = Book.objects.all()[5] 
>>> IndexError: list index out of range
>>> """

>>> We select the last valid index (index 4 corresponds to ID 5, 'Sapiens')
>>> unwanted_book = Book.objects.all()[4]
>>> unwanted_book.delete()
(1, {'bookshelf.Book': 1})

>>> """Verify the deletion
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}, {'id': 2, 'title': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'publication_year': 1979}, {'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}, {'id': 4, 'title': 'Dune', 'author': 'Frank Herbert', 'publication_year': 1965}]>
"""

