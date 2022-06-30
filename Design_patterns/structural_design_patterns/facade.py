"""
Facade Method is a Structural Design pattern that provides a simpler unified
interface to a more complex system. The word Facade means the face of a building
or particularly an outer lying interface of a complex system, consists of several
sub-systems. It is an essential part Gang of Four design patterns. It provides an
easier way to access methods of the underlying systems by providing a single entry
point.
"""

from __future__ import annotations


class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_a())
        results.append(self._subsystem2.operation_b())
        return "\n".join(results)


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: operation1"

    def operation_a(self) -> str:
        return "Subsystem1: operation_a"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: operation1"

    def operation_b(self) -> str:
        return "Subsystem2: operation_b"


def client_code(facade: Facade) -> None:
    print(facade.operation())


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
