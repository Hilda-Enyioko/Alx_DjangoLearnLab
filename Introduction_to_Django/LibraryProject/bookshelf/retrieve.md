# Retrieve: Accessing a Specific Object

>>> """
>>> Incorrect (AttributeError: type object 'Book' has no attribute 'object')
>>> first_book = Book.object.all()[0]
>>> """
>>> """ Correct """
>>> first_book = Book.objects.all()[0]

>>> """ 0R """
>>> second_book = Book.objects.get(publication_year=1989)
>>> print(f"Found book: {second_book.title}")

>>>