"""🧱 Abstract Factory Design Pattern

https://refactoring.guru/design-patterns/abstract-factory

🧠 What is the Factory Design Pattern?
It’s a creational pattern that provides a way to create objects without telling the code which exact class to use.
You let a "factory" object decide which class to create, based on input.

🎯 Why use it?
✅ Advantages:
    Hides object creation logic from the user.
    Easier to manage object creation in one place.
    Adds flexibility: You can add new types without changing the main code.
    Helps with loose coupling – the client code doesn’t depend on specific classes.

⚙️ How does it work?
    Define a common interface or abstract class (IPerson).
    Create multiple concrete classes (Teacher, Student).
    Create a factory class (PersonFactory) with a method (create_person) that:
        Receives a string or key.
        Returns the right object based on the input.

🧱 Abstract Factory Pattern Structure:
    Abstract Factory: Interface for creating related products.
    Concrete Factory: Implements the abstract factory.
    Abstract Products: Interfaces for product families.
    Concrete Products: Specific implementations.
    Client: Works with factories and products through interfaces.

👇 Example from your code:
```
choice = input("Choose a person type (teacher or student): ")
person = PersonFactory.create_person(choice)
person.person_method()
```

If user types "teacher" → the factory returns a Teacher() object.
If user types "student" → the factory returns a Student() object.

"""
from abc import ABCMeta, abstractstaticmethod
import sys

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Interface method"""

class Teacher(IPerson):
    """Teacher"""
    def person_method(self):
        print("I'm a teacher")

class Student(IPerson):
    """Student"""
    def person_method(self):
        print("I'm a student")

class PersonFactory:
    """Factory"""
    @staticmethod
    def create_person(person_type):
        if person_type == "teacher":
            return Teacher()
        elif person_type == "student":
            return Student()
        else:
            raise ValueError("Unknown person type")


# Demo 02
choice = input("Choose a person type (teacher or student): ")
person = PersonFactory.create_person(choice)
person.person_method()

sys.exit(0)

# $ python tuto-07-factory-design-pattern.py
# Choose a person type (teacher or student): teacher
# I'm a teacher

# $ python tuto-07-factory-design-pattern.py
# Choose a person type (teacher or student): abc
# Traceback (most recent call last):
#   File "/home/lavie/dev/work/hoc_them/python-advances/tuto-07-factory-design-pattern.py", line 35, in <module>
#     person = PersonFactory.create_person(choice)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/lavie/dev/work/hoc_them/python-advances/tuto-07-factory-design-pattern.py", line 30, in create_person
#     raise ValueError("Unknown person type")
# ValueError: Unknown person type

##############
# Demo 01
t1 = Teacher()
t1.person_method()

s1 = Student()
s1.person_method()
