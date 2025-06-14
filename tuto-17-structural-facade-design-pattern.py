"""Facade Design Pattern

https://refactoring.guru/design-patterns/facade

🧠 What is the Facade Design Pattern?
The Facade design pattern provides a simplified interface to a complex subsystem.

💡 Purpose:
    Provides a simplified interface to a complex subsystem.
    Simplifies the interaction with the subsystem by hiding its complexity.

🎯 Why use it?
✅ Advantages:
    It provides a simplified interface to a complex subsystem.
    It simplifies the interaction with the subsystem by hiding its complexity.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Facade design pattern provides a simplified interface to a complex subsystem.
    It simplifies the interaction with the subsystem by hiding its complexity.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Facade Pattern Structure:
    Facade – Provides a simplified interface to a complex subsystem.
    Subsystem – The complex subsystem.
    Client – Uses the facade to interact with the subsystem.

🎯 Scenario
You have a complex home theater system with multiple subsystems: DVDPlayer, Projector, Amplifier, and Lights.
Using the Facade pattern, you create a single HomeTheaterFacade class to simplify usage.

🧠 Benefits Demonstrated
    Simplified interaction: The client only needs to deal with the HomeTheaterFacade.
    Decouples the client from subsystem complexity.
    Subsystems can still be used independently if necessary.
"""

# Subsystem classes
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"DVD Player is playing '{movie}'")

    def off(self):
        print("DVD Player is OFF")


class Projector:
    def on(self):
        print("Projector is ON")

    def setWideScreenMode(self):
        print("Projector in widescreen mode")

    def off(self):
        print("Projector is OFF")


class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def setVolume(self, level):
        print(f"Amplifier volume set to {level}")

    def off(self):
        print("Amplifier is OFF")


class Lights:
    def dim(self, level):
        print(f"Lights dimmed to {level}%")

    def on(self):
        print("Lights are ON")

# Facade class
class HomeTheaterFacade:
    def __init__(self, dvd, projector, amp, lights):
        self.dvd = dvd
        self.projector = projector
        self.amp = amp
        self.lights = lights

    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(10)
        self.projector.on()
        self.projector.setWideScreenMode()
        self.amp.on()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def endMovie(self):
        print("Shutting movie theater down...")
        self.dvd.off()
        self.amp.off()
        self.projector.off()
        self.lights.on()


# Client code
if __name__ == "__main__":
    # Create instances of subsystems
    dvd = DVDPlayer()
    projector = Projector()
    amp = Amplifier()
    lights = Lights()

    # Create facade
    homeTheater = HomeTheaterFacade(dvd, projector, amp, lights)

    # Use facade
    homeTheater.watchMovie("Inception")
    print("\n--- Movie Ends ---\n")
    homeTheater.endMovie()

"""
$ python tuto-17-facade-design-pattern.py
Get ready to watch a movie...
Lights dimmed to 10%
Projector is ON
Projector in widescreen mode
Amplifier is ON
Amplifier volume set to 5
DVD Player is ON
DVD Player is playing 'Inception'

--- Movie Ends ---

Shutting movie theater down...
DVD Player is OFF
Amplifier is OFF
Projector is OFF
Lights are ON
"""