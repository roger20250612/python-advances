"""Observer Design Pattern

https://refactoring.guru/design-patterns/observer

🧠 What is the Observer Design Pattern?
The Observer design pattern is a behavioral design pattern that allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

Observer design pattern, which allows one object (the subject) to notify a set of observers when its state changes.

💡 Purpose:
    Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

🎯 Why use it?
✅ Advantages:
    It defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    It allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Observer design pattern allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    It allows you to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Observer Pattern Structure:
    Subject – Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Concrete Subject – Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Observer – Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Concrete Observer – Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    Client – Uses the observer to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

🎯 Scenario
We simulate a weather station that monitors temperature and humidity. When the temperature or humidity changes, the weather station notifies all its observers.

🧩 Key Benefits:
    Notifies all dependents automatically.
    Enables decoupling of objects.

    Loose coupling between the subject and observers.
    Easily add/remove observers at runtime.
    Good for implementing event-driven systems (e.g., UI, data binding, logging).
"""
import sys

# Demo 05 - Async-Safe Observable using asyncio.Lock

import asyncio
from abc import ABC, abstractmethod

# Async Observer
class AsyncObserver(ABC):
    @abstractmethod
    async def update(self, value):
        pass

# Async-Safe Observable
class AsyncObservableTemperature:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._lock = asyncio.Lock()

    async def register(self, observer: AsyncObserver):
        async with self._lock:
            self._observers.append(observer)
            print(f"{observer.__class__.__name__} subscribed.")

    async def unregister(self, observer: AsyncObserver):
        async with self._lock:
            self._observers.remove(observer)
            print(f"{observer.__class__.__name__} unsubscribed.")

    @property
    def temperature(self):
        return self._temperature  # Access outside lock is okay if atomic

    @temperature.setter
    def temperature(self, value):
        raise AttributeError("Use `set_temperature_async()` to set value")

    async def set_temperature_async(self, value):
        async with self._lock:
            print(f"\n[WeatherStation] Async temperature set to {value}°C")
            self._temperature = value
            observers = list(self._observers)
        await asyncio.gather(*(obs.update(value) for obs in observers))

# Concrete Async Observer
class AsyncLogger(AsyncObserver):
    async def update(self, value):
        await asyncio.sleep(0.1)  # Simulate I/O
        print(f"📝 Logger: Recorded {value}°C")

# Async main
async def main():
    station = AsyncObservableTemperature()
    logger = AsyncLogger()

    await station.register(logger)

    await asyncio.gather(
        station.set_temperature_async(22),
        station.set_temperature_async(25),
        station.set_temperature_async(28)
    )

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)

"""
⚠ Notes:
    We override @property's setter to forbid direct temperature = x (forces async safety).
    Use await set_temperature_async(x) to set and notify safely.
    asyncio.gather() sends updates to all observers concurrently.

✅ Summary
Version	Tech Used	Use When…
Thread-safe	threading.Lock	You’re using threads (threading)
Async-safe	asyncio.Lock	You’re using asyncio, coroutines
"""

################################################################################
# Demo 04 - Thread-Safe @property Observable
import threading
from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass

# Thread-safe Observable
class ThreadSafeObservableTemperature:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._lock = threading.Lock()

    def register(self, observer: Observer):
        with self._lock:
            self._observers.append(observer)
            print(f"{observer.__class__.__name__} subscribed.")

    def unregister(self, observer: Observer):
        with self._lock:
            self._observers.remove(observer)
            print(f"{observer.__class__.__name__} unsubscribed.")

    @property
    def temperature(self):
        with self._lock:
            return self._temperature

    @temperature.setter
    def temperature(self, value):
        with self._lock:
            print(f"\n[WeatherStation] Temperature set to {value}°C")
            self._temperature = value
            observers = list(self._observers)  # Copy for safe iteration
        for observer in observers:
            observer.update(value)

# Concrete Observer
class Logger(Observer):
    def update(self, value):
        print(f"📝 Logger: Recorded {value}°C")

# Client using threading
if __name__ == "__main__":
    import time
    from threading import Thread

    station = ThreadSafeObservableTemperature()
    logger = Logger()
    station.register(logger)

    def worker(id, temps):
        for t in temps:
            print(f"Worker-{id} setting temp to {t}")
            station.temperature = t
            time.sleep(0.1)

    t1 = Thread(target=worker, args=(1, [20, 21, 22]))
    t2 = Thread(target=worker, args=(2, [23, 24, 25]))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

sys.exit(0)

################################################################################
# Demo 03 - Triggering Observers
# ✅ Goal:
#     Trigger observer notifications automatically when a property is set (e.g., weather.temperature = 25)
#     No manual set_temperature() or notify() calls needed
from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass

# Subject with property setter
class ObservableTemperature:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register(self, observer: Observer):
        self._observers.append(observer)
        print(f"{observer.__class__.__name__} subscribed.")

    def unregister(self, observer: Observer):
        self._observers.remove(observer)
        print(f"{observer.__class__.__name__} unsubscribed.")

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print(f"\n[WeatherStation] Temperature updated to: {value}°C")
        self._temperature = value
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, value):
        print(f"📱 PhoneDisplay: Temp is now {value}°C")

class Logger(Observer):
    def update(self, value):
        print(f"📝 Logger: Temperature recorded as {value}°C")

# Client code
if __name__ == "__main__":
    weather = ObservableTemperature()

    phone = PhoneDisplay()
    logger = Logger()

    weather.register(phone)
    weather.register(logger)

    # Direct assignment triggers notification
    weather.temperature = 22
    weather.temperature = 27

    weather.unregister(phone)
    weather.temperature = 30

sys.exit(0)

# $ python tuto-24-behavioral-observer-design-pattern.py
# PhoneDisplay subscribed.
# Logger subscribed.

# [WeatherStation] Temperature updated to: 22°C
# 📱 PhoneDisplay: Temp is now 22°C
# 📝 Logger: Temperature recorded as 22°C

# [WeatherStation] Temperature updated to: 27°C
# 📱 PhoneDisplay: Temp is now 27°C
# 📝 Logger: Temperature recorded as 27°C
# PhoneDisplay unsubscribed.

# [WeatherStation] Temperature updated to: 30°C
# 📝 Logger: Temperature recorded as 30°C

# 🧩 Why This is Pythonic:
#     Uses @property to hook into attribute access transparently
#     Clean, idiomatic API (weather.temperature = x)
#     No need for separate set_temperature() method

################################################################################
# Demo 02 - Async Observer using Asyncio
import asyncio
from abc import ABC, abstractmethod

# Abstract Observer
class AsyncObserver(ABC):
    @abstractmethod
    async def update(self, temperature):
        pass

# Subject (Observable)
class AsyncWeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer: AsyncObserver):
        self._observers.append(observer)
        print(f"{observer.__class__.__name__} subscribed.")

    def remove_observer(self, observer: AsyncObserver):
        self._observers.remove(observer)
        print(f"{observer.__class__.__name__} unsubscribed.")

    async def notify_observers(self):
        await asyncio.gather(*(observer.update(self._temperature) for observer in self._observers))

    async def set_temperature(self, temperature):
        print(f"\n[WeatherStation] New temperature: {temperature}°C")
        self._temperature = temperature
        await self.notify_observers()

# Concrete async observers
class AsyncPhoneDisplay(AsyncObserver):
    async def update(self, temperature):
        await asyncio.sleep(0.5)  # Simulate async task
        print(f"📱 PhoneDisplay: Temperature is {temperature}°C")

class AsyncWindowDisplay(AsyncObserver):
    async def update(self, temperature):
        await asyncio.sleep(0.3)  # Simulate async task
        print(f"🪟 WindowDisplay: Now showing {temperature}°C")

class AsyncLogger(AsyncObserver):
    async def update(self, temperature):
        await asyncio.sleep(0.1)  # Simulate async log write
        print(f"📝 Logger: Logged temperature {temperature}°C")

# Main async application
async def main():
    station = AsyncWeatherStation()

    phone = AsyncPhoneDisplay()
    window = AsyncWindowDisplay()
    logger = AsyncLogger()

    station.register_observer(phone)
    station.register_observer(window)
    station.register_observer(logger)

    await station.set_temperature(25)
    await station.set_temperature(30)

    station.remove_observer(window)
    await station.set_temperature(28)

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)

# $ python tuto-24-behavioral-observer-design-pattern.py
# AsyncPhoneDisplay subscribed.
# AsyncWindowDisplay subscribed.
# AsyncLogger subscribed.

# [WeatherStation] New temperature: 25°C
# 📝 Logger: Logged temperature 25°C
# 🪟 WindowDisplay: Now showing 25°C
# 📱 PhoneDisplay: Temperature is 25°C

# [WeatherStation] New temperature: 30°C
# 📝 Logger: Logged temperature 30°C
# 🪟 WindowDisplay: Now showing 30°C
# 📱 PhoneDisplay: Temperature is 30°C
# AsyncWindowDisplay unsubscribed.

# [WeatherStation] New temperature: 28°C
# 📝 Logger: Logged temperature 28°C
# 📱 PhoneDisplay: Temperature is 28°C

"""
✅ Highlights:
    asyncio.gather() notifies all observers concurrently.
    Each observer can do independent async work (e.g., I/O, API calls).
    Clean separation between subject and observers.
"""

################################################################################
# Demo 01 - Observer with Weather Station

from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Subject (Observable)
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)
        print(f"{observer.__class__.__name__} subscribed.")

    def remove_observer(self, observer):
        self._observers.remove(observer)
        print(f"{observer.__class__.__name__} unsubscribed.")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"\n[WeatherStation] New temperature: {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: Temperature updated to {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"WindowDisplay: Now showing {temperature}°C")

# Client code
if __name__ == "__main__":
    station = WeatherStation()

    phone = PhoneDisplay()
    window = WindowDisplay()

    station.register_observer(phone)
    station.register_observer(window)

    station.set_temperature(25)
    station.set_temperature(30)

    station.remove_observer(window)
    station.set_temperature(28)


# $ python tuto-24-behavioral-observer-design-pattern.py
# PhoneDisplay subscribed.
# WindowDisplay subscribed.

# [WeatherStation] New temperature: 25°C
# PhoneDisplay: Temperature updated to 25°C
# WindowDisplay: Now showing 25°C

# [WeatherStation] New temperature: 30°C
# PhoneDisplay: Temperature updated to 30°C
# WindowDisplay: Now showing 30°C
# WindowDisplay unsubscribed.

# [WeatherStation] New temperature: 28°C
# PhoneDisplay: Temperature updated to 28°C
