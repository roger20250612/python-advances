"""Decorator Design Pattern

https://refactoring.guru/design-patterns/decorator

🧠 What is the Decorator Design Pattern?
The Decorator design pattern is a structural design pattern that allows you to add new functionality to an existing object dynamically.

💡 Purpose:
    Adds new functionality to an existing object dynamically.
    Provides a way to extend the functionality of an object without modifying its structure.

🎯 Why use it?
✅ Advantages:
    It adds new functionality to an existing object dynamically.
    It provides a way to extend the functionality of an object without modifying its structure.
    It enables you to add new functionality to an existing object dynamically.

⚙️ How does it work?
    The Decorator design pattern allows you to add new functionality to an existing object dynamically.
    It provides a way to extend the functionality of an object without modifying its structure.
    It enables you to add new functionality to an existing object dynamically.

🧱 Decorator Pattern Structure:
    Component – The object being decorated.
    Concrete Component – The object being decorated.
    Decorator – Implements the functionality to be added.
    Concrete Decorator – Implements the functionality to be added.
    Client – Uses the decorator to add functionality to the component.

🎯 Key Concept:
You “wrap” an object with a decorator, which adds new functionality while maintaining the object’s interface.

📦 Example Scenario:
Imagine you have a text editor. The core text can be decorated with features like:
    Bold text
    Italic text
    Underlined text

🧩 Benefits:
    You can add or remove behavior at runtime.
    Promotes the Open/Closed Principle: open for extension, closed for modification.
    Avoids subclassing explosion (compared to creating many subclasses for combinations).
"""
# Component
class Text:
    def render(self) -> str:
        return "Hello, world!"

# Base Decorator
class TextDecorator(Text):
    def __init__(self, wrapped: Text):
        self._wrapped = wrapped

    def render(self) -> str:
        return self._wrapped.render()

# Concrete Decorators
class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{super().render()}</i>"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{super().render()}</u>"

# Client code
if __name__ == "__main__":
    simple_text = Text()
    print("Plain text:")
    print(simple_text.render())

    print("\nDecorated text:")
    decorated = BoldDecorator(ItalicDecorator(UnderlineDecorator(simple_text)))
    print(decorated.render())

# $ python tuto-16-decorator-design-pattern.py
# Plain text:
# Hello, world!

# Decorated text:
# <b><i><u>Hello, world!</u></i></b>
