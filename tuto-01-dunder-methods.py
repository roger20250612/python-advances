"""
Dunder methods : Double underscore methods, Short for double underscore methods,
                 because their names always begin and end with double underscores (e.g., __init__, __str__, __len__, etc.).
Magic Methods : A commonly used informal term because these methods allow your objects to behave in "magical" ways.
Special Methods : This is the official term used in the Python documentation.
                  These methods enable custom behavior for built-in operations (like addition, string representation, or calling).
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __call__(self, *args, **kwargs):
        print("It is called")

v1 = Vector(5, 10)
v2 = Vector(6, 12)
print(f"v1={v1}")
print(f"v2={v2}")

v3 = v1 + v2
print(f"v3={v3}")

v3()
