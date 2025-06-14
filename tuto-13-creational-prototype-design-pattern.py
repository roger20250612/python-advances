"""Prototype Design Pattern

https://refactoring.guru/design-patterns/prototype

🧠 What is the Prototype Design Pattern?
The Prototype design pattern is a creational design pattern that allows you to create new objects by copying existing ones.

🎯 Why use it?
✅ Advantages:
    It provides a way to create new objects by copying existing ones.
    It allows you to create new objects without knowing the exact class of the original object.
    It enables you to create new objects with the same properties as the original object.

⚙️ How does it work?
    The Prototype design pattern allows you to create new objects by copying existing ones.
    It provides a way to create new objects without knowing the exact class of the original object.
    It enables you to create new objects with the same properties as the original object.

🧱 Prototype Pattern Structure:
    Prototype Interface – Declares a clone() method.
    Concrete Prototype – Implements the clone() method.
    Client – Uses the prototype to create copies.
"""

from abc import ABC, abstractmethod
import copy

# Step 1: Prototype Interface
class Shape(ABC):
    def __init__(self):
        self.color = None

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with color {self.color}"

# Step 2: Concrete Prototypes
class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle with radius {self.radius} and color {self.color}"

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Rectangle {self.width}x{self.height} with color {self.color}"

# Step 3: Client Code
if __name__ == "__main__":
    # Create original objects
    circle = Circle(radius=10)
    circle.color = "Red"

    rectangle = Rectangle(width=5, height=7)
    rectangle.color = "Blue"

    # Clone them
    cloned_circle = circle.clone()
    cloned_rectangle = rectangle.clone()

    # Modify clones
    cloned_circle.color = "Green"
    cloned_rectangle.width = 8

    # Display results
    print("Originals:")
    print(circle)
    print(rectangle)

    print("\nClones:")
    print(cloned_circle)
    print(cloned_rectangle)

# $ python tuto-13-prototype-design-pattern.py
# Originals:
# Circle with radius 10 and color Red
# Rectangle 5x7 with color Blue

# Clones:
# Circle with radius 10 and color Green
# Rectangle 8x7 with color Blue

"""
✅ Key Benefits of the Prototype Pattern:
    Avoids costly initialization of objects.
    Supports dynamic object duplication without depending on their concrete classes.
    Allows polymorphic copying.
"""