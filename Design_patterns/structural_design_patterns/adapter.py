"""
Adapter method helps us in making the incompatible objects adaptable to each other.
The Adapter method is one of the easiest methods to understand because we have a lot
of real-life examples that show the analogy with it. The main purpose of this method
is to create a bridge between two incompatible interfaces. This method provides a
different interface for a class. We can more easily understand the concept by thinking
about the Cable Adapter that allows us to charge a phone somewhere that has outlets in
different shapes. Using this idea, we can integrate the classes that couldn’t be
integrated due to interface incompatibility.
"""


class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def client_incompatible_request(self) -> str:
        return "client the to behaviour Unknown"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        result = self.client_incompatible_request()
        translation = " ".join(list(result.split())[::-1])
        return f"Adapter: (Translated) {translation}"


def client_code(target: Target) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client works fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.client_incompatible_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
