"""Mediator Design Pattern

https://refactoring.guru/design-patterns/mediator

🧠 What is the Mediator Design Pattern?
The Mediator design pattern is a behavioral design pattern that defines an object that encapsulates how a set of objects interact.

💡 Purpose:
    Defines an object that encapsulates how a set of objects interact.
    Allows you to define an object that encapsulates how a set of objects interact.

🎯 Why use it?
✅ Advantages:
    It defines an object that encapsulates how a set of objects interact.
    It allows you to define an object that encapsulates how a set of objects interact.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The Mediator design pattern allows you to define an object that encapsulates how a set of objects interact.
    It allows you to define an object that encapsulates how a set of objects interact.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 Mediator Pattern Structure:
    Mediator – Defines an object that encapsulates how a set of objects interact.
    Concrete Mediator – Defines an object that encapsulates how a set of objects interact.
    Client – Uses the mediator to define an object that encapsulates how a set of objects interact.

🎯 Scenario
We simulate a Chat Room where multiple users communicate only through a central mediator, not directly with each other.

🧩 Key Benefits:
    Loose coupling: Objects communicate through the mediator, not directly.
    Central control: Easy to modify or manage interactions in one place.
    Scalability: Adding new objects doesn't increase complexity exponentially.
"""
import sys

# Demo 03 - Async Message Broker with Asyncio
import asyncio
from collections import defaultdict

class AsyncMessageBroker:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, topic, listener):
        self.subscribers[topic].append(listener)
        print(f"{listener.name} subscribed to '{topic}'")

    def unsubscribe(self, topic, listener):
        if listener in self.subscribers[topic]:
            self.subscribers[topic].remove(listener)
            print(f"{listener.name} unsubscribed from '{topic}'")

    async def publish(self, topic, message):
        print(f"\n[Broker] Publishing to '{topic}': {message}")
        if topic not in self.subscribers or not self.subscribers[topic]:
            print(f"No subscribers for topic '{topic}'")
            return
        # Notify all subscribers concurrently
        await asyncio.gather(
            *(subscriber.receive(topic, message) for subscriber in self.subscribers[topic])
        )

class AsyncSubscriber:
    def __init__(self, name):
        self.name = name

    async def receive(self, topic, message):
        # Simulate async processing delay
        await asyncio.sleep(0.5)
        print(f"{self.name} received on '{topic}': {message}")

async def main():
    broker = AsyncMessageBroker()

    alice = AsyncSubscriber("Alice")
    bob = AsyncSubscriber("Bob")
    charlie = AsyncSubscriber("Charlie")

    broker.subscribe("sports", alice)
    broker.subscribe("news", bob)
    broker.subscribe("sports", charlie)
    broker.subscribe("tech", charlie)

    # Publish messages asynchronously
    await broker.publish("sports", "Team A won the game!")
    await broker.publish("news", "Elections coming next month.")
    await broker.publish("tech", "New Python release is out!")

    # Demonstrate unsubscribe
    broker.unsubscribe("sports", charlie)
    await broker.publish("sports", "Team B scored a goal!")

if __name__ == "__main__":
    asyncio.run(main())

sys.exit(0)

# $ python tuto-22-behavioral-mediator-design-pattern.py
# Alice subscribed to 'sports'
# Bob subscribed to 'news'
# Charlie subscribed to 'sports'
# Charlie subscribed to 'tech'

# [Broker] Publishing to 'sports': Team A won the game!
# Alice received on 'sports': Team A won the game!
# Charlie received on 'sports': Team A won the game!

# [Broker] Publishing to 'news': Elections coming next month.
# Bob received on 'news': Elections coming next month.

# [Broker] Publishing to 'tech': New Python release is out!
# Charlie received on 'tech': New Python release is out!
# Charlie unsubscribed from 'sports'

# [Broker] Publishing to 'sports': Team B scored a goal!
# Alice received on 'sports': Team B scored a goal!

################################################################################
# Demo 02 - Mediator as a Message Broker
# A MessageBroker-style communication is a classic use of the Mediator pattern, often found in systems like RabbitMQ, Kafka, or event buses.
# Here’s a Python implementation of a lightweight Message Broker that allows components to subscribe to and publish messages to topics, without directly referencing each other.

# 🧩 Key Takeaways:
#     Loose coupling: Publishers don't know or care who listens.
#     Dynamic subscription: Subscribers can join/leave topics anytime.
#     Scalable: Easily handles many topics and subscribers.

from collections import defaultdict

# Mediator (Message Broker)
class MessageBroker:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, topic, listener):
        self.subscribers[topic].append(listener)
        print(f"{listener.name} subscribed to '{topic}'")

    def publish(self, topic, message):
        print(f"\n[Broker] Publishing to '{topic}': {message}")
        for listener in self.subscribers[topic]:
            listener.receive(topic, message)

# Subscriber Interface
class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive(self, topic, message):
        print(f"{self.name} received on '{topic}': {message}")

# Client code
if __name__ == "__main__":
    broker = MessageBroker()

    # Subscribers
    alice = Subscriber("Alice")
    bob = Subscriber("Bob")
    charlie = Subscriber("Charlie")

    # Subscribing to topics
    broker.subscribe("sports", alice)
    broker.subscribe("news", bob)
    broker.subscribe("sports", charlie)
    broker.subscribe("tech", charlie)

    # Publishers sending messages to topics
    broker.publish("sports", "Team A won the game!")
    broker.publish("news", "Elections coming next month.")
    broker.publish("tech", "New Python release is out!")

sys.exit(0)

# $ python tuto-22-behavioral-mediator-design-pattern.py
# Alice subscribed to 'sports'
# Bob subscribed to 'news'
# Charlie subscribed to 'sports'
# Charlie subscribed to 'tech'

# [Broker] Publishing to 'sports': Team A won the game!
# Alice received on 'sports': Team A won the game!
# Charlie received on 'sports': Team A won the game!

# [Broker] Publishing to 'news': Elections coming next month.
# Bob received on 'news': Elections coming next month.

# [Broker] Publishing to 'tech': New Python release is out!
# Charlie received on 'tech': New Python release is out!

################################################################################
# Demo 01 - Mediator with Chat Room
from abc import ABC, abstractmethod

# Mediator Interface
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self.participants = []

    def register(self, user):
        self.participants.append(user)

    def send_message(self, message, sender):
        for user in self.participants:
            if user != sender:
                user.receive(message, sender)

# Colleague (User) Interface
class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.register(self)

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message, sender):
        pass

# Concrete User
class ConcreteUser(User):
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message, sender):
        print(f"{self.name} receives from {sender.name}: {message}")

# Client code
if __name__ == "__main__":
    chatroom = ChatRoom()

    alice = ConcreteUser("Alice", chatroom)
    bob = ConcreteUser("Bob", chatroom)
    charlie = ConcreteUser("Charlie", chatroom)

    alice.send("Hello, everyone!")
    print()
    bob.send("Hi Alice!")

# $ python tuto-22-behavioral-mediator-design-pattern.py
# Alice sends: Hello, everyone!
# Bob receives from Alice: Hello, everyone!
# Charlie receives from Alice: Hello, everyone!

# Bob sends: Hi Alice!
# Alice receives from Bob: Hi Alice!
# Charlie receives from Bob: Hi Alice!
