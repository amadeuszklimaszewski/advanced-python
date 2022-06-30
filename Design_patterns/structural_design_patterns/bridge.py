""" 
Bridge is a structural design pattern that divides business logic or huge class
into separate class hierarchies that can be developed independently.
"""

from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "Concrete implementation A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "Concrete implementation B."


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementation2 = ConcreteImplementationB()
    abstraction2 = ExtendedAbstraction(implementation2)
    client_code(abstraction2)
