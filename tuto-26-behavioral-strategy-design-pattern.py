"""Strategy Design Pattern

https://refactoring.guru/design-patterns/strategy

🧠 What is the Strategy Design Pattern?
The Strategy design pattern is a behavioral design pattern that allows you to select an algorithm at runtime.

💡 Purpose:
    Select an algorithm at runtime.
    Allows you to select an algorithm at runtime.

🎯 Why use it?
✅ Advantages:
    It selects an algorithm at runtime.
    It allows you to select an algorithm at runtime.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Strategy design pattern allows you to select an algorithm at runtime.
    It allows you to select an algorithm at runtime.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Strategy Pattern Structure:
    Strategy – Selects an algorithm at runtime.
    Concrete Strategy – Selects an algorithm at runtime.
    Client – Uses the strategy to select an algorithm at runtime.

🎯 Scenario
We simulate a payment system where the user can pay with a credit card or a bank transfer.

Suppose you’re building a payment processing system that supports multiple payment methods: Credit Card, PayPal, and Bitcoin.
Instead of hardcoding logic for each, you define them as interchangeable strategies.

🧩 Key Benefits:
    Selects the algorithm at runtime.
    Allows you to change the algorithm without modifying the client code.

    Strategy interface (PaymentStrategy): defines the common interface.
    Concrete strategies implement different algorithms.
    Context (PaymentContext) delegates work to the strategy object.
    Flexibility: You can switch strategies at runtime without modifying the context.
"""

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal account {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin wallet {self.wallet_address}")

# Context Class
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

# Client Code
if __name__ == "__main__":
    # Choose payment strategy at runtime
    context = PaymentContext(CreditCardPayment("1234-5678-9012-3456"))
    context.checkout(100)

    context.set_strategy(PayPalPayment("user@example.com"))
    context.checkout(200)

    context.set_strategy(BitcoinPayment("1FfmbHfnpaZjKFvyi1okTjJJusN455paPH"))
    context.checkout(300)

# $ python tuto-26-behavioral-strategy-design-pattern.py
# Paid $100 using Credit Card 1234-5678-9012-3456
# Paid $200 using PayPal account user@example.com
# Paid $300 using Bitcoin wallet 1FfmbHfnpaZjKFvyi1okTjJJusN455paPH
