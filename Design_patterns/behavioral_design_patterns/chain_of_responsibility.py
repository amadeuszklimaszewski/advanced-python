"""
Chain of Responsibility method is Behavioral design pattern and
it is the object-oriented version of if … elif … elif … else and
make us capable to rearrange the condition-action blocks dynamically
at the run-time. It allows us to pass the requests along the chain
of handlers. The processing is simple, whenever any handler received
the request it has two choices either to process it or pass it to
the next handler in the chain.

This pattern aims to decouple the senders of a request from its
receivers by allowing the request to move through chained receivers
until it is handled.


there’s a slightly different approach (and it’s a bit more canonical)
in which, upon receiving a request, a handler decides whether it can
process it. If it can, it doesn’t pass the request any further. So it’s
either only one handler that processes the request or none at all. This
approach is very common when dealing with events in stacks of elements
within a graphical user interface.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class RequestAHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "RequestA":
            return f"RequestAHandler: I'll handle {request}"
        else:
            return super().handle(request)


class RequestBHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "RequestB":
            return f"RequestBHandler: I'll handle {request}"
        else:
            return super().handle(request)


class RequestCHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "RequestC":
            return f"RequestCHandler: I'll handle {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    for request in ["RequestA", "RequestB", "RequestC", "RequestD"]:
        print(f"\nClient: Who will handle {request}?")
        result = handler.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")


if __name__ == "__main__":
    request_a_handler = RequestAHandler()
    request_b_handler = RequestBHandler()
    request_c_handler = RequestCHandler()

    request_a_handler.set_next(request_b_handler).set_next(request_c_handler)

    print("Chain: RequestAHandler > RequestBHandler > RequestCHandler")
    client_code(request_a_handler)
    print("\n")

    print("Subchain: RequestBHandler > RequestCHandler")
    client_code(request_b_handler)
