
# Python Advanced Tutorials

+ https://refactoring.guru/design-patterns

+ https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc
NeuralNine

# Create venv

uv : https://github.com/astral-sh/uv
An extremely fast Python package and project manager, written in Rust.

🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
⚡️ 10-100x faster than pip.

uv is backed by Astral, the creators of Ruff.

Step 1: Init project
```bash
$ uv init
```
Initialized project `sample-codes`

Step 2: Create an Virtual Environment
```bash
$ uv venv
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

Step 3: Activate .venv
```bash
$ source .venv/bin/activate
```

When implementing **Object-Oriented Programming (OOP)** in Python, it's important to understand and apply the following core concepts and related principles. Here's a comprehensive list of important points:

---

## 🧱 **Core OOP Principles**

1. ### **Encapsulation**

   * Bundling data (attributes) and methods (functions) into a single unit (class).
   * Hiding internal state and requiring all interaction through methods.
   * Access modifiers in Python:

     * `public` (default): accessible from anywhere.
     * `protected` (`_name`): meant for internal use only (convention).
     * `private` (`__name`): name mangling to prevent direct access.

2. ### **Inheritance**

   * Creating a new class from an existing class (parent-child relationship).
   * Enables **code reuse** and **extensibility**.
   * Use `super()` to call the parent class’s methods or constructor.

3. ### **Polymorphism**

   * Same interface for different underlying data types.
   * Method overriding: subclass provides a specific implementation of a method defined in the parent class.
   * Duck typing in Python: “If it quacks like a duck...”

4. ### **Abstraction**

   * Hiding complex implementation details and exposing only the essential features.
   * Achieved using abstract classes and interfaces.
   * Use `abc` module (`ABC`, `@abstractmethod`).

---

## 🛠️ **Other Important Concepts & Best Practices**

5. ### **Class and Object**

   * A **class** is a blueprint; an **object** is an instance of a class.

6. ### **Constructors**

   * Special method `__init__()` is used to initialize object attributes.

7. ### **Class Variables vs Instance Variables**

   * Class variables are shared across all instances.
   * Instance variables are unique to each object.

8. ### **Static Methods and Class Methods**

   * `@staticmethod`: doesn’t access class or instance.
   * `@classmethod`: receives class as the first argument (`cls`).

9. ### **Magic Methods / Dunder Methods**

   * Special methods like `__str__`, `__repr__`, `__eq__`, `__len__`, `__add__`, etc.
   * Used for operator overloading and customizing class behavior.

10. ### **Composition over Inheritance**

* Prefer combining simple objects to create more complex functionality instead of deep inheritance trees.

11. ### **Multiple Inheritance**

* Python supports multiple inheritance.
* Use with care to avoid ambiguity (MRO – Method Resolution Order).

12. ### **Properties and Getters/Setters**

* Use `@property` and setter decorators to control access to private attributes.

13. ### **Type Annotations**

* Use type hints for attributes and method parameters/returns for readability and static analysis.

14. ### **Data Classes (Python 3.7+)**

* Use `@dataclass` for classes mainly storing data (auto-generates `__init__`, `__repr__`, etc.).

15. ### **Design Patterns**

* Familiarize with common OOP patterns: Singleton, Factory, Observer, etc.

---

## ✅ Example Skeleton

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self._name = name  # encapsulation

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self._name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self._name} says Meow!"

def animal_sound(animal: Animal):
    print(animal.speak())  # polymorphism

dog = Dog("Buddy")
cat = Cat("Whiskers")
animal_sound(dog)
animal_sound(cat)
```

---

Would you like a visual diagram or cheat sheet to go with this?
