# Update: Modifying an Existing Record

>>> first_book.publication_year = 2019
>>> first_book.save()
>>> Book.objects.all().values()[0]
{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2019}

# Reverting the change
>>> first_book.publication_year = 2018
>>> first_book.save()
>>> Book.objects.all().values()[0]
{'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'publication_year': 2018}

