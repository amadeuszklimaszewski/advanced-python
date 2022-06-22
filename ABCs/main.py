from abc import ABC, abstractmethod

# Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated, and require subclasses to provide
# implementations for the abstract methods.


class MediaLoader(ABC):
    @abstractmethod
    def play(self) -> None:
        ...

    @property
    @abstractmethod
    def ext(self) -> str:
        ...


class InvalidWav(MediaLoader):
    pass


class Ogg(MediaLoader):
    ext = ".ogg"

    def play(self):
        pass


if __name__ == "__main__":
    print(MediaLoader.__abstractmethods__)
    try:
        x = InvalidWav()
    except TypeError as exc:
        print(exc)
    o = Ogg()
    print(o)
