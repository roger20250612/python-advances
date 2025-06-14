"""Multiple Inheritance

Multiple inheritance is a feature of object-oriented programming languages that
allows a class to inherit from multiple parent classes.

🧠 What is it?
Multiple inheritance is a way to combine multiple classes into one.
It allows you to inherit from multiple classes, which can be useful when you want to reuse code from multiple sources.

🎯 Why use it?
✅ Advantages:
    You can reuse code from multiple sources.
    Allows you to inherit from multiple classes.
    Allows you to define common behavior in multiple classes.
    Allows you to define common attributes in multiple classes.
    Allows you to override methods in multiple classes.

⚙️ How does it work?
    You can define multiple parent classes in a class definition.
    The class inherits from all of them.
    The class also inherits from the classes in the order they are defined.
    When you call a method on an object, Python looks at the object's class and its parent classes in the order they are defined.
    If the method is not found in the current class, it looks at the parent classes in the order they are defined.

"""

class Father:
    def skills(self):
        print("Father: Gardening, Carpenting")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits skills:")
        super().skills()  # Calls method based on MRO
        Mother.skills(self)  # Explicit call

# Check Method Resolution Order (MRO)
print("MRO:", [cls.__name__ for cls in Child.__mro__])

# Instantiate and call
child = Child()
child.skills()

# $ python tuto-05-multiple-inheritance.py
# MRO: ['Child', 'Father', 'Mother', 'object']
# Child inherits skills:
# Father: Gardening, Carpenting
# Mother: Cooking, Painting

"""
🧠 Explanation:
    The Child class inherits from both Father and Mother.
    super().skills() calls the Father.skills() method first, because Father appears before Mother in the inheritance list.
    Python uses C3 linearization to determine the MRO (Method Resolution Order).
    Mother.skills(self) is called explicitly to demonstrate calling both parent methods manually.

⚠️ Tips:
    Be cautious with multiple inheritance as it can lead to conflicts if both parents have methods with the same name.
    Always check and understand the MRO to avoid surprises.
    Use super() only when you’re sure the method exists in the next class in the MRO.
"""