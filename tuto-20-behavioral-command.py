"""Command Design Pattern

https://refactoring.guru/design-patterns/command

🧠 What is the Command Design Pattern?
The Command design pattern is a behavioral design pattern that encapsulates a request as an object,
thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

💡 Purpose:
    Encapsulates a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.
    Allows you to encapsulate a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

🎯 Why use it?
✅ Advantages:
    It encapsulates a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.
    It allows you to encapsulate a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Command design pattern allows you to encapsulate a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.
    It allows you to encapsulate a request as an object, thereby allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Command Pattern Structure:
    Command – Encapsulates a request as an object.
    Concrete Command – Encapsulates a request as an object.
    Client – Uses the command to encapsulate a request as an object.

🎯 Scenario
We simulate a remote control that can execute and undo commands like turning on/off a light and a fan. Each action is encapsulated as a command object.

🧩 Key Benefits:
    Encapsulates actions as objects.
    Enables undo/redo functionality.
    Supports logging, queuing, and macro commands.
"""

# Demo 02 - Command Queue
import sys
from abc import ABC, abstractmethod
from time import sleep

# Receiver classes
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Fan:
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()

# Invoker with queue support
class CommandQueue:
    def __init__(self):
        self.queue = []

    def add_command(self, command):
        print(f"Queued: {command.__class__.__name__}")
        self.queue.append(command)

    def run_all(self, delay_seconds=0):
        print("\nExecuting queued commands...")
        while self.queue:
            command = self.queue.pop(0)
            command.execute()
            if delay_seconds > 0:
                sleep(delay_seconds)

# Client code
if __name__ == "__main__":
    light = Light()
    fan = Fan()

    queue = CommandQueue()

    # Queue commands
    queue.add_command(LightOnCommand(light))
    queue.add_command(FanOnCommand(fan))
    queue.add_command(LightOffCommand(light))
    queue.add_command(FanOffCommand(fan))

    # Execute all with a delay of 1 second between commands
    queue.run_all(delay_seconds=1)

sys.exit(0)

# $ python tuto-20-behavioral-command.py
# Queued: LightOnCommand
# Queued: FanOnCommand
# Queued: LightOffCommand
# Queued: FanOffCommand

# Executing queued commands...
# Light is ON
# Fan is ON
# Light is OFF
# Fan is OFF

################################################################################
# Demo 01
from abc import ABC, abstractmethod

# Receiver classes
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class Fan:
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

    def undo(self):
        self.fan.turn_off()

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()

    def undo(self):
        self.fan.turn_on()

# Invoker class
class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command):
        command.execute()
        self.history.append(command)

    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo.")

# Client code
if __name__ == "__main__":
    light = Light()
    fan = Fan()

    # Create command objects
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    remote = RemoteControl()

    # Execute some commands
    remote.press_button(light_on)
    remote.press_button(fan_on)
    remote.press_button(light_off)

    # Undo last command
    print("\nUndoing last command:")
    remote.press_undo()
    print("Undoing another command:")
    remote.press_undo()

# $ python tuto-20-behavioral-command.py
# Light is ON
# Fan is ON
# Light is OFF

# Undoing last command:
# Light is ON
# Undoing another command:
# Fan is OFF
