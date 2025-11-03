# Retrieve: Accessing a Specific Object

>>> # Incorrect (AttributeError: type object 'Book' has no attribute 'object')
>>> # first_book = Book.object.all()[0]

>>> # Correct
>>> first_book = Book.objects.all()[0]

>>> # 0R
>>> second_book = Book.objects.all()[1]
>>> print(f"Found book: {second_book.title}")

>>>