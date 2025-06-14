"""Factory Method Design Pattern

https://refactoring.guru/design-patterns/factory-method

🧠 What is the Factory Method Design Pattern?
The Factory Method design pattern is a creational design pattern that provides a way to create objects without telling the code which exact class to use.
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

🔧 Concept:
    Factory Method defines an interface for creating an object.
    Subclasses decide which class to instantiate.
    Promotes loose coupling and extensibility.

🧱 Structure:
    Product (Abstract) – declares interface.
    ConcreteProduct – implements Product.
    Creator (Factory class) – declares factory method.
    ConcreteCreator – implements factory method.
"""

from abc import ABC, abstractmethod

# Step 1: Product Interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Step 2: Concrete Products
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box."

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a container."

# Step 3: Creator Abstract Class
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        result = transport.deliver()
        print(f"[Logistics] {result}")

# Step 4: Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Step 5: Client Code
def client_code(logistics: Logistics):
    logistics.plan_delivery()

# Test
if __name__ == "__main__":
    print("App: Launched with RoadLogistics.")
    client_code(RoadLogistics())

    print("\nApp: Launched with SeaLogistics.")
    client_code(SeaLogistics())

# $ python tuto-11-factory-method-design-pattern.py
# App: Launched with RoadLogistics.
# [Logistics] Delivering by land in a box.

# App: Launched with SeaLogistics.
# [Logistics] Delivering by sea in a container.

"""
✅ Key Benefits of Factory Method:
    Code is open for extension but closed for modification.
    Decouples object creation from its usage.
    Easy to introduce new transport types without changing the core logic.
"""