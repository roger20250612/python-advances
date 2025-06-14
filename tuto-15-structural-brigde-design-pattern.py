"""Bridge Design Pattern

https://refactoring.guru/design-patterns/bridge

🧠 What is the Bridge Design Pattern?
The Bridge design pattern is a structural design pattern that allows you to decouple an abstraction from its implementation.

💡 Purpose:
    Separates an abstraction from its implementation.
    Provides a way to replace one abstraction with another without modifying the client code.

🎯 Why use it?
✅ Advantages:
    It separates an abstraction from its implementation.
    It provides a way to replace one abstraction with another without modifying the client code.
    It enables you to decouple an abstraction from its implementation.

⚙️ How does it work?
    The Bridge design pattern separates an abstraction from its implementation.
    It provides a way to replace one abstraction with another without modifying the client code.
    It enables you to decouple an abstraction from its implementation.

🧱 Bridge Pattern Structure:
    Abstraction – The abstraction being replaced.
    Implementor – The class that implements the abstraction.
    Concrete Implementor – The class that implements the abstraction.
    Client – The code that uses the abstraction.

🧠 Key Concepts:
    Abstraction (RemoteControl) delegates the work to the implementation (Device).
    Abstraction and implementation can be extended independently.
    You can mix and match remotes with devices dynamically.
"""

# Implementation hierarchy
class Device:
    def is_enabled(self) -> bool:
        raise NotImplementedError()

    def enable(self):
        raise NotImplementedError()

    def disable(self):
        raise NotImplementedError()

    def set_volume(self, percent: int):
        raise NotImplementedError()

class TV(Device):
    def __init__(self):
        self._on = False
        self._volume = 30

    def is_enabled(self) -> bool:
        return self._on

    def enable(self):
        self._on = True
        print("TV is now ON.")

    def disable(self):
        self._on = False
        print("TV is now OFF.")

    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f"TV volume set to {self._volume}.")

class Radio(Device):
    def __init__(self):
        self._on = False
        self._volume = 50

    def is_enabled(self) -> bool:
        return self._on

    def enable(self):
        self._on = True
        print("Radio is now ON.")

    def disable(self):
        self._on = False
        print("Radio is now OFF.")

    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f"Radio volume set to {self._volume}.")

# Abstraction hierarchy
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        print("Decreasing volume by 10.")
        self.device.set_volume(10)

    def volume_up(self):
        print("Increasing volume by 10.")
        self.device.set_volume(90)

# Extended abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Muting device.")
        self.device.set_volume(0)

# Client code
if __name__ == "__main__":
    tv = TV()
    remote = AdvancedRemoteControl(tv)

    remote.toggle_power()
    remote.volume_up()
    remote.mute()
    remote.toggle_power()

    print("\n---\n")

    radio = Radio()
    remote2 = RemoteControl(radio)

    remote2.toggle_power()
    remote2.volume_down()
    remote2.toggle_power()

# $ python tuto-15-structural-brigde-design-pattern.py
# TV is now ON.
# Increasing volume by 10.
# TV volume set to 90.
# Muting device.
# TV volume set to 0.
# TV is now OFF.

# ---

# Radio is now ON.
# Decreasing volume by 10.
# Radio volume set to 10.
# Radio is now OFF.
