"""🌳 Adapter Design Pattern

https://refactoring.guru/design-patterns/adapter

🧠 What is the Adapter Design Pattern?
The Adapter design pattern is a structural design pattern that allows you to work with two incompatible interfaces by
creating a third interface that makes them work together.

💡 Purpose:
    Adapts the interface of an existing class to another interface that clients expect.
    Allows classes with incompatible interfaces to work together.

🎯 Why use it?
✅ Advantages:
    It allows you to work with two incompatible interfaces by creating a third interface that makes them work together.
    It provides a way to adapt the interface of an existing class to another interface that clients expect.
    It enables classes with incompatible interfaces to work together.

⚙️ How does it work?
    The Adapter design pattern allows you to work with two incompatible interfaces by creating a third interface that
    makes them work together.
    It provides a way to adapt the interface of an existing class to another interface that clients expect.
    It enables classes with incompatible interfaces to work together.

🧱 Adapter Pattern Structure:
    Target Interface – The interface expected by the client.
    Adaptee – The incompatible class with useful functionality.
    Adapter – Implements the target interface and translates calls to the adaptee.
"""

# Step 1: Target Interface expected by the client
class AmericanPlug:
    def plug_in(self):
        return "Plugged into American socket."

# Step 2: Adaptee with incompatible interface
class EuropeanSocket:
    def connect(self):
        return "Connected to European socket."

# Step 3: Adapter to make EuropeanSocket compatible with AmericanPlug interface
class SocketAdapter(AmericanPlug):
    def __init__(self, european_socket: EuropeanSocket):
        self.european_socket = european_socket

    def plug_in(self):
        # Translate American plug interface to European socket interface
        return self.european_socket.connect()

# Step 4: Client code using AmericanPlug interface
def client_code(plug: AmericanPlug):
    print(plug.plug_in())

# Step 5: Usage
if __name__ == "__main__":
    print("Using American plug directly:")
    american_plug = AmericanPlug()
    client_code(american_plug)

    print("\nUsing European socket with Adapter:")
    european_socket = EuropeanSocket()
    adapter = SocketAdapter(european_socket)
    client_code(adapter)

# $ python tuto-14-structural-adapter-design-pattern.py
# Using American plug directly:
# Plugged into American socket.

# Using European socket with Adapter:
# Connected to European socket.

"""
Context
    Suppose you have a client that expects to work with an interface called AmericanPlug, which has a method .plug_in().
    However, you want to use an existing class EuropeanSocket that doesn’t have the .plug_in() method; instead, it has .connect().
    These two interfaces are incompatible.
    The Adapter pattern solves this by wrapping the EuropeanSocket inside an adapter that translates .plug_in() calls into .connect() calls.

✅ Why use Adapter?
    Allows classes with incompatible interfaces to work together.
    Enhances reusability of existing classes.
    Avoids modifying existing code.
"""