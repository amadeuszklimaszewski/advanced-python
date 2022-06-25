# The Template method is a Behavioral Design Pattern that defines the
# skeleton of the operation and leaves the details to be implemented by
# the child class. Its subclasses can override the method implementations
# as per need but the invocation is to be in the same way as defined by
# an abstract class. It is one of the easiest among the Behavioral design
# pattern to understand and implements. Such methods are highly used in
# framework development as they allow us to reuse the single piece of
# code at different places by making certain changes. This leads to
# avoiding code duplication also.

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:

    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
