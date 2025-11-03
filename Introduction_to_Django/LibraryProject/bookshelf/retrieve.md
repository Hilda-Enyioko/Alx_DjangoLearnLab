# Retrieve: Accessing a Specific Object

# Incorrect (AttributeError: type object 'Book' has no attribute 'object')
# >>> first_book = Book.object.all()[0]

# Correct
>>> first_book = Book.objects.all()[0]

