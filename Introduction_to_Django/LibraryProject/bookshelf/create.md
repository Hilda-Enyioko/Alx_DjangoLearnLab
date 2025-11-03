## Create: Adding the First Book

>>> book = Book(title='Atomic Habits', author='James Clear', publication_year=2018)
>>> book.save()
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}]>

OR 

>>> Book.objects.create(
  title='The Lord of the Rings'
  author='J.R.R. Tolkien',
  publication_year=1954
)

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

# Verify all entries exist
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}, {'id': 2, 'title': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'publication_year': 1979}, {'id': 3, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}, {'id': 4, 'title': 'Dune', 'author': 'Frank Herbert', 'publication_year': 00}, {'id': 5, 'title': 'Sapiens: A Brief History of Humankind', 'author': 'Yuval Noah Harari', 'publication_year': 2014}]>

