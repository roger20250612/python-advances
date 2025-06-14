"""Chain of Responsibility Design Pattern

https://refactoring.guru/design-patterns/chain-of-responsibility

🧠 What is the Chain of Responsibility Design Pattern?
The Chain of Responsibility design pattern is a behavioral design pattern that allows you to handle requests in a sequential order.

💡 Purpose:
    Handle requests in a sequential order.
    Allows you to handle requests in a sequential order.

🎯 Why use it?
✅ Advantages:
    It handles requests in a sequential order.
    It allows you to handle requests in a sequential order.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Chain of Responsibility design pattern allows you to handle requests in a sequential order.
    It allows you to handle requests in a sequential order.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Chain of Responsibility Pattern Structure:
    Handler – Handles a request.
    Concrete Handler – Handles a request.
    Concrete Handler – Handles a request.
    Client – Uses the chain of responsibility to handle a request.

🎯 Scenario
We simulate a support system where different levels of staff handle issues depending on severity:
    Frontline Support: Handles minor issues.
    Supervisor: Handles moderate issues.
    Manager: Handles serious issues.

🧩 Key Features:
    set_next() links handlers dynamically.
    Each handler decides whether to process or pass on.
    Easy to add new handlers without modifying existing code.
"""

from abc import ABC, abstractmethod

# Abstract handler
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # Enables chaining

    @abstractmethod
    def handle(self, request):
        pass

# Concrete handler 1
class FrontlineSupport(Handler):
    def handle(self, request):
        if request < 3:
            print(f"FrontlineSupport: Handled issue level {request}")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print(f"FrontlineSupport: Cannot handle issue level {request}")

# Concrete handler 2
class Supervisor(Handler):
    def handle(self, request):
        if 3 <= request < 6:
            print(f"Supervisor: Handled issue level {request}")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print(f"Supervisor: Cannot handle issue level {request}")

# Concrete handler 3
class Manager(Handler):
    def handle(self, request):
        if request >= 6:
            print(f"Manager: Handled issue level {request}")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print(f"Manager: Cannot handle issue level {request}")

# Client code
if __name__ == "__main__":
    # Create handlers
    frontline = FrontlineSupport()
    supervisor = Supervisor()
    manager = Manager()

    # Build the chain
    frontline.set_next(supervisor).set_next(manager)

    # Sample requests with varying severity
    for issue in [1, 4, 7, 0, 5]:
        print(f"\nClient: Who can handle issue level {issue}?")
        frontline.handle(issue)

# $ python tuto-19-behavioral-chain-of-responsibility.py

# Client: Who can handle issue level 1?
# FrontlineSupport: Handled issue level 1

# Client: Who can handle issue level 4?
# Supervisor: Handled issue level 4

# Client: Who can handle issue level 7?
# Manager: Handled issue level 7

# Client: Who can handle issue level 0?
# FrontlineSupport: Handled issue level 0

# Client: Who can handle issue level 5?
# Supervisor: Handled issue level 5
