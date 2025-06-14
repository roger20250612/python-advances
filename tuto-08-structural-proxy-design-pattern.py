"""Proxy Design Pattern

https://refactoring.guru/design-patterns/proxy

✅ What is the Proxy Design Pattern?
The Proxy Pattern is like a middleman between a client and a real object.
It lets you control access to the real object.

🧠 Why use it?
You use a proxy when:
    🔐 You want to check permissions before allowing access.
    🕒 You want to delay loading something heavy until it’s really needed.
    📊 You want to log, count, or monitor when an object is used.
    🌐 The real object is on a remote server, and the proxy connects to it.

💡 Simple Example
Imagine a video player app:
    Videos are large and slow to load.
    You use a VideoProxy that only loads the real video when the user clicks play.

🎯 In short:
    A proxy is a helper object that controls access to something — it can add security, reduce cost, or add extra behavior.

💡 How does it work?
    The proxy object is a wrapper around the real object.
    It controls access to the real object.
    It can also add extra behavior.
    The proxy object can be used exactly like the real object.

"""
import sys
from abc import ABCMeta, abstractmethod
from typing import Any

class IPerson(metaclass=ABCMeta):
    """Interface"""
    @abstractmethod
    def person_method(self) -> None:
        """Interface method"""

class Person:
    """Concrete implementation"""
    def person_method(self) -> None:
        print("I'm a person")

class PersonProxy(IPerson):
    """Proxy that wraps a real Person object"""
    def __init__(self, person: IPerson) -> None:
        self.person = person

    def person_method(self):
        print("I'm a proxy")
        self.person.person_method()

class PersonFactory:
    """Factory for creating IPerson instances"""

    @staticmethod
    def create_person(person_type: str) -> IPerson:
        if person_type == "person":
            return Person()
        elif person_type == "proxy":
            return PersonProxy(Person())
        else:
            raise ValueError("Unknown person type")

# Demo 02
choice = input("Choose a person type (person or proxy): ").strip().lower()
try:
    person = PersonFactory.create_person(choice)
    person.person_method()
except ValueError as e:
    print(e)

sys.exit(0)

# $ python tuto-08-proxy-design-pattern.py
# Choose a person type (person or proxy): proxy
# I'm a proxy
# I'm a person

# $ python tuto-08-proxy-design-pattern.py
# Choose a person type (person or proxy): cb
# Unknown person type
