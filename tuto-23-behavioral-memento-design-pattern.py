"""Memento Design Pattern

https://refactoring.guru/design-patterns/memento

🧠 What is the Memento Design Pattern?
The Memento design pattern is a behavioral design pattern that allows you to capture and externalize an object's internal state.

The Memento pattern is used to capture and externalize an object’s internal state so that it can be restored later,
without violating encapsulation.

💡 Purpose:
    Capture and externalize an object's internal state.
    Allows you to capture and externalize an object's internal state.

🎯 Why use it?
✅ Advantages:
    It captures and externalize an object's internal state.
    It allows you to capture and externalize an object's internal state.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Memento design pattern allows you to capture and externalize an object's internal state.
    It allows you to capture and externalize an object's internal state.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Memento Pattern Structure:
    Memento – Captures an object's internal state.
    Concrete Memento – Captures an object's internal state.
    Client – Uses the memento to externalize an object's internal state.

    Originator: The object whose state needs to be saved and restored.
    Memento: Stores the internal state of the Originator.
    Caretaker: Manages the Memento but doesn't access or modify its content.

🎯 Scenario
We simulate a game where the player can save the game state to a memento, and reload it later.

🧩 Key Benefits:
    Captures the state of an object.
    Allows you to externalize the state of an object.
    Enables you to restore the state of an object.
"""

# Memento: stores the state of the Originator
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


# Originator: creates a Memento and uses it to restore its state
class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state: str):
        print(f"Originator: Setting state to '{state}'")
        self._state = state

    def get_state(self) -> str:
        return self._state

    def save_to_memento(self) -> Memento:
        print(f"Originator: Saving to Memento with state '{self._state}'")
        return Memento(self._state)

    def restore_from_memento(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: State restored to '{self._state}'")


# Caretaker: keeps a list of Mementos
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: Memento):
        self._mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self._mementos[index]


# Example usage
if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State #1")
    caretaker.add_memento(originator.save_to_memento())

    originator.set_state("State #2")
    caretaker.add_memento(originator.save_to_memento())

    originator.set_state("State #3")
    print("Current State:", originator.get_state())

    print("\nRestoring previous state...")
    originator.restore_from_memento(caretaker.get_memento(0))

    print("\nRestoring another previous state...")
    originator.restore_from_memento(caretaker.get_memento(1))

# $ python tuto-23-behavioral-memento-design-pattern.py
# Originator: Setting state to 'State #1'
# Originator: Saving to Memento with state 'State #1'
# Originator: Setting state to 'State #2'
# Originator: Saving to Memento with state 'State #2'
# Originator: Setting state to 'State #3'
# Current State: State #3

# Restoring previous state...
# Originator: State restored to 'State #1'

# Restoring another previous state...
# Originator: State restored to 'State #2'
