# Builder lets you construct complex objects step by step.
# The pattern allows you to produce different types and representations
# of an object using the same construction code


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Product:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product:
    def __init__(self) -> None:
        self.parts: list[Any] = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder=builder)

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()
    print("\n")

    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()

    custom_product = builder.product
    custom_product.list_parts()

    print("\n")

    print("Builder product after reset: ")
    builder.product.list_parts()
