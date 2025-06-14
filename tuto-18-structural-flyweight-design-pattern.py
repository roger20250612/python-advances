"""Flyweight Design Pattern

https://refactoring.guru/design-patterns/flyweight

🧠 What is the Flyweight Design Pattern?
The Flyweight design pattern is a software design pattern that allows you to reduce the cost of creating and manipulating a large number of similar objects.

💡 Purpose:
    Reduce the cost of creating and manipulating a large number of similar objects.
    Improve performance by reusing existing objects.

🎯 Why use it?
✅ Advantages:
    It reduces the cost of creating and manipulating a large number of similar objects.
    It improves performance by reusing existing objects.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Flyweight design pattern allows you to reduce the cost of creating and manipulating a large number of similar objects.
    It improves performance by reusing existing objects.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Flyweight Pattern Structure:
    Flyweight – Represents a flyweight object.
    Concrete Flyweight – Represents a flyweight object.
    Client – Uses the flyweight to represent a flyweight object.

🎯 Scenario
Imagine a text editor rendering millions of characters.
Instead of storing font style, size, and color for each character, we store it once per style, and just reuse it.

🧠 Key Takeaways
    Flyweight (TextStyle): stores shared, immutable data.
    Factory: reuses existing flyweights instead of creating new ones.
    Extrinsic state (Character.symbol): kept outside to remain unique.
"""
# Flyweight class: Shared state
class TextStyle:
    def __init__(self, font_family, font_size, bold, italic):
        self.font_family = font_family
        self.font_size = font_size
        self.bold = bold
        self.italic = italic

    def __str__(self):
        return f"Font({self.font_family}, {self.font_size}px, Bold={self.bold}, Italic={self.italic})"

# Flyweight Factory: Ensures shared instances
class TextStyleFactory:
    _styles = {}

    @classmethod
    def get_style(cls, font_family, font_size, bold, italic):
        key = (font_family, font_size, bold, italic)
        if key not in cls._styles:
            cls._styles[key] = TextStyle(*key)
        return cls._styles[key]

# Context class: Contains extrinsic state
class Character:
    def __init__(self, symbol, style):
        self.symbol = symbol            # Extrinsic (unique per object)
        self.style = style              # Intrinsic (shared)

    def render(self, position):
        print(f"Render '{self.symbol}' at {position} with style [{self.style}]")

# Client code
if __name__ == "__main__":
    factory = TextStyleFactory()

    # Shared style for most characters
    normal_style = factory.get_style("Arial", 12, False, False)

    # A different style for headings
    bold_style = factory.get_style("Arial", 14, True, False)

    # Create text document with mixed styles
    document = [
        Character("H", bold_style),
        Character("e", normal_style),
        Character("l", normal_style),
        Character("l", normal_style),
        Character("o", normal_style),
    ]

    # Render document
    for i, char in enumerate(document):
        char.render((i, 0))  # (x, y) position

# $ python tuto-18-flyweight-design-pattern.py
# Render 'H' at (0, 0) with style [Font(Arial, 14px, Bold=True, Italic=False)]
# Render 'e' at (1, 0) with style [Font(Arial, 12px, Bold=False, Italic=False)]
# Render 'l' at (2, 0) with style [Font(Arial, 12px, Bold=False, Italic=False)]
# Render 'l' at (3, 0) with style [Font(Arial, 12px, Bold=False, Italic=False)]
# Render 'o' at (4, 0) with style [Font(Arial, 12px, Bold=False, Italic=False)]
