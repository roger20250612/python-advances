"""Polymorphism

🧠 What is it?
Polymorphism is a feature of object-oriented programming languages that allows objects of different classes to be treated as objects of a common superclass.

🎯 Why use it?
✅ Advantages:
    Allows you to write code that can work with objects of different classes.
    Enables you to write code that can work with objects of different classes without knowing their specific types.
    Enables you to write code that can work with objects of different classes without knowing their specific types.
    Makes your code more flexible and adaptable.

⚙️ How does it work?
    Polymorphism is achieved through method overriding and method overloading.
    Method overriding is when a subclass provides its own implementation of a method that is already defined in its superclass.
    Method overloading is when a class provides multiple methods with the same name but different parameters.
"""

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Polymorphic function
def make_animal_speak(animal: Animal):
    print(f"{animal.__class__.__name__} says: {animal.speak()}")

# Create instances
animals = [Dog(), Cat(), Cow()]

# Use same interface (speak) for different types
for animal in animals:
    make_animal_speak(animal)

# $ python tuto-05-polymorphism.py
# Dog says: Woof!
# Cat says: Meow!
# Cow says: Moo!

"""
🧠 Explanation
    All classes share the same interface: speak().
    Subclasses override speak() with their own behavior.
    The function make_animal_speak() accepts any object that is an Animal and calls the appropriate speak() method—polymorphism in action.

💡 Notes:
    Python supports runtime polymorphism (i.e., the method that's called is determined at runtime).
    Unlike some languages, Python doesn’t require formal interfaces—duck typing lets you write flexible code that works on any object with the expected method(s).
"""