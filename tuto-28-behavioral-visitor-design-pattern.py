"""Visitor Design Pattern

https://refactoring.guru/design-patterns/visitor

🧠 What is the Visitor Design Pattern?
The Visitor design pattern is a behavioral design pattern that allows you to define a new operation
without changing the classes of the objects on which it operates.

💡 Purpose:
    Defines a new operation without changing the classes of the objects on which it operates.
    Allows you to define a new operation without changing the classes of the objects on which it operates.

🎯 Why use it?
✅ Advantages:
    It defines a new operation without changing the classes of the objects on which it operates.
    It allows you to define a new operation without changing the classes of the objects on which it operates.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Visitor design pattern allows you to define a new operation without changing the classes of the objects on which it operates.
    It allows you to define a new operation without changing the classes of the objects on which it operates.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Visitor Pattern Structure:
    Visitor – Defines a new operation without changing the classes of the objects on which it operates.
    Concrete Visitor – Defines a new operation without changing the classes of the objects on which it operates.
    Client – Uses the visitor to define a new operation without changing the classes of the objects on which it operates.

🎯 Scenario
We simulate a weather station that monitors temperature and humidity. When the temperature or humidity changes, the weather station notifies all its observers.

Let’s say you’re building a document editor with elements like Text, Image, and Table.
You want to add operations like exporting to HTML or counting words, but without changing the element classes themselves.

🧩 Key Benefits:
    Notifies all dependents automatically.
    Enables decoupling of objects.

    Elements define accept(visitor) which calls visitor.visit_xxx(self).
    Visitors encapsulate operations and can be added without changing the element classes.
    Makes it easy to add new behaviors to an object structure.
"""

from abc import ABC, abstractmethod

# Visitor Interface
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_text(self, element): pass

    @abstractmethod
    def visit_image(self, element): pass

    @abstractmethod
    def visit_table(self, element): pass

# Element Interface
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: DocumentVisitor): pass

# Concrete Elements
class Text(DocumentElement):
    def __init__(self, content):
        self.content = content

    def accept(self, visitor: DocumentVisitor):
        visitor.visit_text(self)

class Image(DocumentElement):
    def __init__(self, path):
        self.path = path

    def accept(self, visitor: DocumentVisitor):
        visitor.visit_image(self)

class Table(DocumentElement):
    def __init__(self, rows):
        self.rows = rows

    def accept(self, visitor: DocumentVisitor):
        visitor.visit_table(self)

# Concrete Visitor 1: Export to HTML
class HtmlExportVisitor(DocumentVisitor):
    def visit_text(self, element):
        print(f"<p>{element.content}</p>")

    def visit_image(self, element):
        print(f"<img src='{element.path}' />")

    def visit_table(self, element):
        print("<table>")
        for row in element.rows:
            print("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
        print("</table>")

# Concrete Visitor 2: Word Counter
class WordCountVisitor(DocumentVisitor):
    def __init__(self):
        self.word_count = 0

    def visit_text(self, element):
        self.word_count += len(element.content.split())

    def visit_image(self, element):
        pass  # No words in images

    def visit_table(self, element):
        for row in element.rows:
            for cell in row:
                self.word_count += len(str(cell).split())

    def get_count(self):
        return self.word_count

# Client Code
if __name__ == "__main__":
    # Document elements
    elements = [
        Text("Hello world!"),
        Image("logo.png"),
        Table([["Name", "Age"], ["Alice", "30"], ["Bob", "25"]])
    ]

    # Use HTML export visitor
    print("Exporting document to HTML:")
    html_visitor = HtmlExportVisitor()
    for el in elements:
        el.accept(html_visitor)

    # Use Word count visitor
    print("\nCounting words in document:")
    count_visitor = WordCountVisitor()
    for el in elements:
        el.accept(count_visitor)
    print(f"Total words: {count_visitor.get_count()}")

# $ python tuto-28-behavioral-visitor-design-pattern.py
# Exporting document to HTML:
# <p>Hello world!</p>
# <img src='logo.png' />
# <table>
# <tr><td>Name</td><td>Age</td></tr>
# <tr><td>Alice</td><td>30</td></tr>
# <tr><td>Bob</td><td>25</td></tr>
# </table>

# Counting words in document:
# Total words: 8
