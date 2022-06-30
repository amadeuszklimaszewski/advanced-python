"""
Iterator method is a Behavioral Design Pattern that allows us
to traverse the elements of the collections without taking the
exposure of in-depth details of the elements. It provides a way
to access the elements of complex data structure sequentially
without repeating them.

According to GangOfFour, Iterator Pattern is used ” to access
the elements of an aggregate object sequentially without exposing
its underlying implementation”.
"""

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class InOrderIterator(Iterator):
    _position: int = None

    _reverse: bool = False

    def __init__(self, collection: Iterable, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> InOrderIterator:
        return InOrderIterator(self._collection)

    def get_reverse_iterator(self) -> InOrderIterator:
        return InOrderIterator(self._collection, reverse=True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
