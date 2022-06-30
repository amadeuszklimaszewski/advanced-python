"""
Command Method is Behavioral Design Pattern that encapsulates a request
as an object, thereby allowing for the parameterization of clients
with different requests and the queuing or logging of requests.
Parameterizing other objects with different requests in our analogy
means that the button used to turn on the lights can later be used
to turn on stereo or maybe open the garage door. It helps in promoting
the “invocation of a method on an object” to full object status.
Basically, it encapsulates all the information needed to perform an
action or trigger an event.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(
            f"SimpleCommand: See, I can do simple things like printing"
            f"({self._payload})"
        )


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a})", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b})", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Beginning process...")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something important...")

        print("Invoker: ...finishing process...")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

    invoker.do_something_important()
