"""Abstraction

🧠 What is it?
Abstraction is a feature of object-oriented programming languages that allows you to create abstract classes and methods.

🎯 Why use it?
✅ Advantages:
    Hides implementation details.
    Provides a high-level interface for working with objects.
    Allows you to work with objects without worrying about their internal implementation.
    Enables you to write code that is more flexible and adaptable.

⚙️ How does it work?
    Abstraction is achieved through abstract classes and abstract methods.
    An abstract class is a class that cannot be instantiated.
    It can only be used as a base class for other classes.
    An abstract method is a method that is declared in an abstract class but does not have an implementation.
"""

from abc import ABC, abstractmethod

# Abstract base class
class BankAccount(ABC):
    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def deposit(self, amount: float):
        pass

    def get_balance(self):
        return self._balance

# Concrete implementation for a savings account
class SavingsAccount(BankAccount):
    def withdraw(self, amount: float):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}")

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Deposited ${amount}")

# Usage
account = SavingsAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Balance for {account._owner}: ${account.get_balance()}")

# $ python tuto-05-abstraction.py
# Deposited $500
# Withdrew $300
# Balance for Alice: $1200

"""
🧩 Explanation:
    BankAccount is an abstract class that defines the interface (withdraw and deposit).
    SavingsAccount provides the concrete implementation, hiding how the balance is managed internally.
    Users only see simple, essential methods; complex logic like validation and balance handling is abstracted away.

💡 Key Points:
    Use ABC as a base class.
    Decorate methods with @abstractmethod to force implementation in subclasses.
    You cannot instantiate an abstract class directly.
"""