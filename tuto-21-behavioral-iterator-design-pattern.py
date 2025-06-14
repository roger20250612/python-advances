"""Iterator Design Pattern

https://refactoring.guru/design-patterns/iterator

🧠 What is the Iterator Design Pattern?
The Iterator design pattern is a behavioral design pattern that allows you to traverse a collection of data.

💡 Purpose:
    Traverse a collection of data.
    Allows you to traverse a collection of data.

🎯 Why use it?
✅ Advantages:
    It traverses a collection of data.
    It allows you to traverse a collection of data.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Iterator design pattern allows you to traverse a collection of data.
    It allows you to traverse a collection of data.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Iterator Pattern Structure:
    Iterator – Defines an interface for traversing a collection of data.
    Concrete Iterator – Defines an interface for traversing a collection of data.
    Client – Uses the iterator to traverse a collection of data.

🎯 Scenario
We'll build a custom collection (like a container of books), and an iterator to traverse it
without exposing the internal structure (like a list).

🧩 Key Benefits:
    Traverses elements without exposing how they're stored.
    Can easily adapt to linked lists, trees, or graphs.
    Supports multiple independent iterators for the same collection.
"""

# Demo 02 - Iterator with Linked List
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

    def __reversed__(self):
        return ReverseBookIterator(self._books)

# Forward Iterator
class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book

# Reverse Iterator
class ReverseBookIterator:
    def __init__(self, books):
        self._books = books
        self._index = len(books) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        book = self._books[self._index]
        self._index -= 1
        return book

# Client code
if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book(Book("1984"))
    collection.add_book(Book("Brave New World"))
    collection.add_book(Book("Fahrenheit 451"))

    print("Forward iteration:\n")
    for book in collection:
        print(book)

    print("\nReverse iteration:\n")
    for book in reversed(collection):
        print(book)

# $ python tuto-21-behavioral-iterator-design-pattern.py
# Forward iteration:

# Book: 1984
# Book: Brave New World
# Book: Fahrenheit 451

# Reverse iteration:

# Book: Fahrenheit 451
# Book: Brave New World
# Book: 1984
# Traversing books using iterator:

# Book: 1984
# Book: Brave New World
# Book: Fahrenheit 451

################################################################################
# Demo 01 - Iterator
from abc import ABC, abstractmethod

# The Item to be stored
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Concrete Iterator
class BookIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._position = 0

    def has_next(self):
        return self._position < len(self._books)

    def next(self):
        if self.has_next():
            book = self._books[self._position]
            self._position += 1
            return book
        else:
            raise StopIteration("No more books.")

# Collection interface
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Concrete Collection
class BookCollection(IterableCollection):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def create_iterator(self):
        return BookIterator(self._books)

# Client code
if __name__ == "__main__":
    # Create collection and add items
    collection = BookCollection()
    collection.add_book(Book("1984"))
    collection.add_book(Book("Brave New World"))
    collection.add_book(Book("Fahrenheit 451"))

    # Get an iterator
    iterator = collection.create_iterator()

    print("Traversing books using iterator:\n")
    while iterator.has_next():
        book = iterator.next()
        print(book)

# $ python tuto-21-behavioral-iterator-design-pattern.py
# Traversing books using iterator:

# Book: 1984
# Book: Brave New World
# Book: Fahrenheit 451
