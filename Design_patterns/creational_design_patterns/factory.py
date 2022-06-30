"""
Factory Method allows an interface or a class to create an object,
but lets subclasses decide which class or object to instantiate.
Using the Factory method, we have the best ways to create an object.
Here, objects are created without exposing the logic to the client,
and for creating the new type of object, the client uses the same
common interface.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(
        f"Client: Exact creator subclass is unknown, but it still works using dependency inversion.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("Now using the ConcreteCreator1...")
    client_code(ConcreteCreator1())
    print("\n")

    print("Now using the ConcreteCreator2...")
    client_code(ConcreteCreator2())
