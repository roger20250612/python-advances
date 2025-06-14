"""Builder Design Pattern

https://refactoring.guru/design-patterns/builder

🧠 What is the Builder Design Pattern?
The Builder design pattern is a creational design pattern that separates the construction of a complex object
from its representation.

🎯 Why use it?
✅ Advantages:
    Separates construction from representation.
    Encapsulates the complexity of object creation.
    Simplifies the process of creating objects.
    Enables easy extension and modification of object creation.

⚙️ How does it work?
    Define a common interface or abstract class (IPerson).
    Create multiple concrete classes (Teacher, Student).
    Create a builder class (PersonBuilder) with a method (create_person) that:
        Receives a string or key.
        Returns the right object based on the input.

🧱 Builder Pattern Structure:
    Product – The complex object being built.
    Builder (Abstract) – Declares building steps.
    ConcreteBuilder – Implements the building steps.
    Director – Controls the building sequence.
    Client – Initiates the building process.
"""

from abc import ABC, abstractmethod

# Step 1: Product
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls}, {self.doors}, {self.windows}, and {self.roof}"

# Step 2: Builder Interface
class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self): pass

    @abstractmethod
    def build_doors(self): pass

    @abstractmethod
    def build_windows(self): pass

    @abstractmethod
    def build_roof(self): pass

    @abstractmethod
    def get_result(self) -> House: pass

# Step 3: Concrete Builder
class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden walls"

    def build_doors(self):
        self.house.doors = "wooden doors"

    def build_windows(self):
        self.house.windows = "glass windows"

    def build_roof(self):
        self.house.roof = "wooden roof"

    def get_result(self) -> House:
        return self.house

class StoneHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "stone walls"

    def build_doors(self):
        self.house.doors = "metal doors"

    def build_windows(self):
        self.house.windows = "reinforced windows"

    def build_roof(self):
        self.house.roof = "stone roof"

    def get_result(self) -> House:
        return self.house

# Step 4: Director
class ConstructionEngineer:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()

    def get_house(self) -> House:
        return self.builder.get_result()

# Step 5: Client Code
if __name__ == "__main__":
    print("Constructing a Wooden House:")
    wooden_builder = WoodenHouseBuilder()
    engineer = ConstructionEngineer(wooden_builder)
    engineer.construct_house()
    house = engineer.get_house()
    print(house)

    print("\nConstructing a Stone House:")
    stone_builder = StoneHouseBuilder()
    engineer = ConstructionEngineer(stone_builder)
    engineer.construct_house()
    house = engineer.get_house()
    print(house)

# $ python tuto-12-builder-design-pattern.py
# Constructing a Wooden House:
# House with wooden walls, wooden doors, glass windows, and wooden roof

# Constructing a Stone House:
# House with stone walls, metal doors, reinforced windows, and stone roof

"""
✅ Benefits of Builder Pattern:
    Separation of construction logic from the final object.
    Allows step-by-step construction of complex objects.
    Supports creation of different representations using the same steps.
"""