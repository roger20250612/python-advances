"""🌳 Composite Design Pattern

https://refactoring.guru/design-patterns/composite

🧠 What is the Composite Design Pattern?
The Composite design pattern is a structural design pattern that allows you to treat a group of objects as a single object.

💡 Purpose:
    Compose objects into tree structures to represent part-whole hierarchies.
    Treat individual objects and compositions of objects uniformly.

🎯 Why use it?
✅ Advantages:
    It allows you to treat a group of objects as a single object.
    It provides a way to manage complex relationships between objects.
    It can be used to represent hierarchical structures, trees, or graphs.

⚙️ How does it work?
    The Composite design pattern allows you to treat a group of objects as a single object.
    It provides a way to manage complex relationships between objects.
    It can be used to represent hierarchical structures, trees, or graphs.
"""

# Demo 02 - Files and folders in a file system
import sys
from abc import ABC, abstractmethod

# Component
class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent: int = 0):
        pass

# Leaf
class File(FileSystemItem):
    def __init__(self, name: str):
        self.name = name

    def show(self, indent: int = 0):
        print(" " * indent + f"- File: {self.name}")

# Composite
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self._children = []

    def add(self, item: FileSystemItem):
        self._children.append(item)

    def remove(self, item: FileSystemItem):
        self._children.remove(item)

    def show(self, indent: int = 0):
        print(" " * indent + f"+ Folder: {self.name}")
        for child in self._children:
            child.show(indent + 2)

# Usage
root = Folder("root")
home = Folder("home")
documents = Folder("documents")
pictures = Folder("pictures")

file1 = File("resume.pdf")
file2 = File("photo.jpg")
file3 = File("todo.txt")

documents.add(file1)
pictures.add(file2)
home.add(documents)
home.add(pictures)
root.add(home)
root.add(file3)

root.show()
sys.exit(0)

# $ python tuto-10-composite-design-pattern.py
# + Folder: root
#   + Folder: home
#     + Folder: documents
#       - File: resume.pdf
#     + Folder: pictures
#       - File: photo.jpg
#   - File: todo.txt

"""
🧠 Explanation:
    FileSystemItem: Abstract base class for both files (leaf) and folders (composites).
    File: A leaf node, can't contain other items.
    Folder: A composite, can contain files or other folders.
    The .show() method demonstrates the uniform treatment of both files and folders—recursive tree traversal.

✅ Benefits:
    Simplifies client code by treating individual items and groups uniformly.
    Naturally models hierarchical structures (e.g., GUI trees, company org charts).
"""

###########
# Demo 01
class Component:
    def __init__(self, name):
        self.name = name

class Leaf(Component):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

class Composite(Component):
    def __init__(self, name, components):
        super().__init__(name)
        self.components = components

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def get_components(self):
        return self.components

# Usage
leaf1 = Leaf("Leaf 1", 10)
leaf2 = Leaf("Leaf 2", 20)
leaf3 = Leaf("Leaf 3", 30)

composite = Composite("Composite", [leaf1, leaf2, leaf3])

print("Leaf 1:", leaf1.name, leaf1.value)
print("Leaf 2:", leaf2.name, leaf2.value)
print("Leaf 3:", leaf3.name, leaf3.value)

print("Composite:", composite.name)
print("Components:", composite.get_components())

# $ python tuto-10-composite-design-pattern.py
# Leaf 1: Leaf 1 10
# Leaf 2: Leaf 2 20
# Leaf 3: Leaf 3 30
# Composite: Composite
# Components: [<__main__.Leaf object at 0x7f7c0a0f1d10>, <__main__.Leaf object at 0x7f7c0a0f1d50>, <__main__.Leaf object at 0x7f7c0a0f1da0>]

"""
🧠 Explanation:
    The Composite design pattern allows you to treat a group of objects as a single object.
    It provides a way to manage complex relationships between objects.
    It can be used to represent hierarchical structures, trees, or graphs.

🔐 Why Use This Version?
    It's clean, reusable, and thread-safe in most single-threaded applications.
    Ideal for managing complex relationships between objects.
"""