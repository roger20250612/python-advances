"""Singleton Design Pattern

https://refactoring.guru/design-patterns/singleton

🧠 What is the Singleton Design Pattern?
The Singleton design pattern is a creational design pattern that restricts the instantiation of a class to one object.
It ensures that only one instance of a class is created and provides a global point of access to it.

💡 Purpose:
    Control access to shared resources (e.g., configuration, database connection).
    Ensure a class has only one instance and provide a global point of access to it.

🎯 Why use it?
✅ Advantages:
    It provides a global point of access to a shared resource.
    It ensures that only one instance of a class is created.
    It provides a way to control access to the shared resource.
    It can be used to implement logging, caching, and other shared resources.

⚙️ How does it work?
    The Singleton design pattern restricts the instantiation of a class to one object.
    It ensures that only one instance of a class is created.
    It provides a global point of access to it.
    It can be used to implement logging, caching, and other shared resources.
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # First time: create and store instance
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {
            "debug": True,
            "db_host": "localhost",
            "db_port": 5432,
        }

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings[key] = value

# Usage
config1 = AppConfig()
config2 = AppConfig()

config1.set("debug", False)

print("Config 1 debug:", config1.get("debug"))  # False
print("Config 2 debug:", config2.get("debug"))  # False

print("Same instance?", config1 is config2)     # True

# $ python tuto-09-singleton-design-pattern.py
# Config 1 debug: False
# Config 2 debug: False
# Same instance? True

"""
🧠 Explanation:
    SingletonMeta is a metaclass that overrides __call__() to ensure only one instance of the class is created.
    AppConfig uses this metaclass, making it a singleton.
    config1 and config2 point to the same instance.

🔐 Why Use This Version?
    It's clean, reusable, and thread-safe in most single-threaded applications.
    Ideal for logging, configuration, caching, or database management objects.
"""