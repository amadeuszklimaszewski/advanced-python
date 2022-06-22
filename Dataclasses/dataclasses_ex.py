# Data classes are just regular classes that are geared towards storing state, rather than containing a lot of logic.
# Every time you create a class that mostly consists of attributes, you make a data class.

# What the dataclasses module does is to make it easier to create data classes.
# It takes care of a lot of boilerplate for you.

# This is especially useful when your data class must be hashable; because this requires a __hash__ method as well as an __eq__ method.
# If you add a custom __repr__ method for ease of debugging, that can become quite verbose.

from dataclasses import dataclass


class Item:
    name: str
    price: float
    inventory_quantity: int = 0

    def __init__(self, name: str, price: float, inventory_quantity: int = 0) -> None:
        self.name = name
        self.price = price
        self.inventory_quantity = inventory_quantity

    def get_total(self) -> float:
        return self.price * self.inventory_quantity

    def __repr__(self) -> str:
        return (
            "InventoryItem("
            f"name={self.name!r}, unit_price={self.price!r}, "
            f"inventory_quantity={self.inventory_quantity!r})"
        )

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.inventory_quantity))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return (self.name, self.price, self.inventory_quantity) == (
            other.name,
            other.price,
            other.inventory_quantity,
        )


@dataclass
class ItemDC:
    name: str
    price: float
    inventory_quantity: int = 0

    def get_total(self) -> float:
        return self.price * self.inventory_quantity


@dataclass(
    init=True,  # If true, a __init__() method will be generated.
    repr=True,  # If true, a __repr__() method will be generated.
    eq=True,  # If true, an __eq__() method will be generated.
    order=False,  # If true, __lt__(), __le__(), __gt__(), and __ge__() methods will be generated.
    unsafe_hash=False,  # If False, a __hash__() method is generated according to how eq and frozen are set.
    frozen=False,  # If true, assigning to fields will generate an exception. This emulates read-only frozen instances.
    match_args=True,  # If true (the default is True), the __match_args__ tuple will be created from the list of parameters to the generated __init__() method.
    kw_only=False,  # If true, then all fields will be marked as keyword-only.
    slots=False,  # If true, __slots__ attribute will be generated and new class will be returned instead of the original one.
)
class SomeClass:
    ...


if __name__ == "__main__":
    apple = Item(name="apple", price=4.0, inventory_quantity=10)
    apple_dc = ItemDC(name="apple", price=4.0, inventory_quantity=10)
    apple_dc2 = ItemDC(name="apple", price=4.0, inventory_quantity=10)

    print(apple.get_total())
    print(apple_dc.get_total())
    print(apple_dc == apple)  # >>> False
    print(apple_dc == apple_dc2)  # >>> True

    print(apple)
    print(apple_dc)
