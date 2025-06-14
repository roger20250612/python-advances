"""Multiple Inheritance - More Advanced

💎 Diamond Problem in Python (Multiple Inheritance)
Diamond problem—a classic issue that Python handles using C3 Linearization (MRO)

🔧 Real-World Analogy:
Imagine you're building a system for vehicles.
    Vehicle: base class
    ElectricVehicle and GasVehicle: both extend Vehicle
    HybridVehicle: inherits from both ElectricVehicle and GasVehicle
"""
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class ElectricVehicle(Vehicle):
    def start(self):
        print("Electric system check...")
        super().start()
        print("Electric system check...-Done")

class GasVehicle(Vehicle):
    def start(self):
        print("Fuel system check...")
        super().start()
        print("Fuel system check...-Done")

class HybridVehicle(ElectricVehicle, GasVehicle):
    def start(self):
        print("Hybrid startup initiated:")
        super().start()  # Uses MRO to determine call order
        print("Hybrid startup initiated...-Done")

# Show the MRO
print("MRO:", [cls.__name__ for cls in HybridVehicle.__mro__])

# Instantiate and test
car = HybridVehicle()
car.start()

# $ python tuto-05-multiple-inheritance-more-advanced.py
# MRO: ['HybridVehicle', 'ElectricVehicle', 'GasVehicle', 'Vehicle', 'object']
# Hybrid startup initiated:
# Electric system check...
# Fuel system check...
# Vehicle starting...
# Fuel system check...-Done
# Electric system check...-Done
# Hybrid startup initiated...-Done

# $ python tuto-05-multiple-inheritance-more-advanced.py
# MRO: ['HybridVehicle', 'ElectricVehicle', 'GasVehicle', 'Vehicle', 'object']
# Hybrid startup initiated:
# Electric system check...
# Fuel system check...
# Vehicle starting...

"""
🔍 Explanation
    HybridVehicle inherits from both ElectricVehicle and GasVehicle.
    super().start() in HybridVehicle triggers the MRO chain:
        ElectricVehicle.start() → GasVehicle.start() → Vehicle.start()
    Python uses MRO to avoid duplicate calls and circular references.

⚠️ Why this matters:
    This solves the diamond problem without ambiguity.
    Each class in the hierarchy calls super().start() safely without knowing the full inheritance chain.
    Avoids calling the same method twice if all classes properly use super().
"""