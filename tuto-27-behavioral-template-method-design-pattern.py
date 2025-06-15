"""Template Method Design Pattern

https://refactoring.guru/design-patterns/template-method

🧠 What is the Template Method Design Pattern?
The Template Method design pattern is a behavioral design pattern that allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.

💡 Purpose:
    Defines the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    Allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.

🎯 Why use it?
✅ Advantages:
    It defines the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    It allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Template Method design pattern allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    It allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Template Method Pattern Structure:
    Template Method – Defines the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    Concrete Template Method – Defines the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    Client – Uses the template method to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.

🎯 Scenario
We simulate a base class that defines the skeleton of an algorithm, and let subclasses override specific steps of the algorithm without changing its structure.

Let’s say we’re building a data mining framework that reads data from different file formats (CSV, JSON, XML). The high-level steps are the same: open file → parse data → analyze → close file, but each file format parses data differently.

🧩 Key Benefits:
    Defines the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
    Allows you to define the skeleton of an algorithm in a base class, and let subclasses override specific steps of the algorithm without changing its structure.
"""
from abc import ABC, abstractmethod

# Abstract Class: Template Method defines the skeleton
class DataMiner(ABC):
    def mine(self):
        self.open_file()
        data = self.parse_data()
        self.analyze_data(data)
        self.close_file()

    def open_file(self):
        print("Opening file...")

    @abstractmethod
    def parse_data(self):
        pass

    def analyze_data(self, data):
        print(f"Analyzing data: {data}")

    def close_file(self):
        print("Closing file.\n")

# Concrete Class 1
class CSVDataMiner(DataMiner):
    def parse_data(self):
        print("Parsing CSV data...")
        return "name,age\nAlice,30\nBob,25"

# Concrete Class 2
class JSONDataMiner(DataMiner):
    def parse_data(self):
        print("Parsing JSON data...")
        return '{"employees":[{"name":"Alice","age":30},{"name":"Bob","age":25}]}'

# Concrete Class 3
class XMLDataMiner(DataMiner):
    def parse_data(self):
        print("Parsing XML data...")
        return "<employees><employee><name>Alice</name><age>30</age></employee></employees>"

# Client Code
if __name__ == "__main__":
    print("Using CSV DataMiner:")
    csv_miner = CSVDataMiner()
    csv_miner.mine()

    print("Using JSON DataMiner:")
    json_miner = JSONDataMiner()
    json_miner.mine()

    print("Using XML DataMiner:")
    xml_miner = XMLDataMiner()
    xml_miner.mine()

# $ python tuto-27-behavioral-template-method-design-pattern.py
# Using CSV DataMiner:
# Opening file...
# Parsing CSV data...
# Analyzing data: name,age
# Alice,30
# Bob,25
# Closing file.

# Using JSON DataMiner:
# Opening file...
# Parsing JSON data...
# Analyzing data: {"employees":[{"name":"Alice","age":30},{"name":"Bob","age":25}]}
# Closing file.

# Using XML DataMiner:
# Opening file...
# Parsing XML data...
# Analyzing data: <employees><employee><name>Alice</name><age>30</age></employee></employees>
# Closing file.
