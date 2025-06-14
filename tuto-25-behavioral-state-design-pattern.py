"""State Design Pattern

https://refactoring.guru/design-patterns/state

🧠 What is the State Design Pattern?
The State design pattern is a behavioral design pattern that allows you to associate a context with an object in a way that
it can vary independently from other objects.

The State pattern allows an object to change its behavior dynamically when its internal state changes. It encapsulates different behaviors for different states in separate state classes, and delegates to the current state object.

💡 Purpose:
    Associates a context with an object in a way that it can vary independently from other objects.
    Allows you to associate a context with an object in a way that it can vary independently from other objects.

🎯 Why use it?
✅ Advantages:
    It associates a context with an object in a way that it can vary independently from other objects.
    It allows you to associate a context with an object in a way that it can vary independently from other objects.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

⚙️ How does it work?
    The State design pattern allows you to associate a context with an object in a way that it can vary independently from other objects.
    It allows you to associate a context with an object in a way that it can vary independently from other objects.
    It promotes the Open/Closed Principle: open for extension, closed for modification.
    It enables you to change the internal implementation of the subsystem without affecting the client code.

🧱 State Pattern Structure:
    State – Associates a context with an object in a way that it can vary independently from other objects.
    Concrete State – Associates a context with an object in a way that it can vary independently from other objects.
    Client – Uses the state to associate a context with an object in a way that it can vary independently from other objects.

🎯 Scenario
We’ll model a Document Editor with three states:
    DraftState: Content can be edited.
    ModerationState: Content is pending review.
    PublishedState: Content is read-only.

🧩 Key Benefits:
    Notifies all dependents automatically.
    Enables decoupling of objects.

✅ Key Points:
    Document delegates behavior to its current State.
    You can add/remove states easily without changing Document.
    Behavior changes at runtime depending on state.
"""

from abc import ABC, abstractmethod

# Context
class Document:
    def __init__(self):
        self._state = DraftState(self)
        self.content = ""

    def change_state(self, new_state):
        print(f"Transitioning to {new_state.__class__.__name__}")
        self._state = new_state

    def write(self, text):
        self._state.write(text)

    def publish(self):
        self._state.publish()

    def reject(self):
        self._state.reject()


# State Interface
class State(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def write(self, text): pass

    @abstractmethod
    def publish(self): pass

    @abstractmethod
    def reject(self): pass


# Concrete States
class DraftState(State):
    def write(self, text):
        self.document.content += text
        print(f"[Draft] Writing content: {text}")

    def publish(self):
        print("[Draft] Submitting for review...")
        self.document.change_state(ModerationState(self.document))

    def reject(self):
        print("[Draft] Cannot reject. Already in draft.")


class ModerationState(State):
    def write(self, text):
        print("[Moderation] Cannot edit. Under review.")

    def publish(self):
        print("[Moderation] Approved and published.")
        self.document.change_state(PublishedState(self.document))

    def reject(self):
        print("[Moderation] Rejected. Returning to draft.")
        self.document.change_state(DraftState(self.document))


class PublishedState(State):
    def write(self, text):
        print("[Published] Cannot write. Document is read-only.")

    def publish(self):
        print("[Published] Already published.")

    def reject(self):
        print("[Published] Cannot reject. Document already published.")


# Client code
if __name__ == "__main__":
    doc = Document()
    doc.write("Hello, this is the draft.\n")
    doc.publish()    # Move to Moderation
    doc.write("More content...")  # Should not allow
    doc.reject()     # Back to Draft
    doc.write("Adding after rejection.\n")
    doc.publish()    # Move to Moderation
    doc.publish()    # Move to Published
    doc.write("Attempting to write in published.")  # Not allowed

# $ python tuto-25-behavioral-state-design-pattern.py
# [Draft] Writing content: Hello, this is the draft.

# [Draft] Submitting for review...
# Transitioning to ModerationState
# [Moderation] Cannot edit. Under review.
# [Moderation] Rejected. Returning to draft.
# Transitioning to DraftState
# [Draft] Writing content: Adding after rejection.

# [Draft] Submitting for review...
# Transitioning to ModerationState
# [Moderation] Approved and published.
# Transitioning to PublishedState
# [Published] Cannot write. Document is read-only.
