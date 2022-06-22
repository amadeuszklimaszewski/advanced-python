from dataclasses import dataclass
from enum import Enum, auto


class InvalidPaymentTypeException(Exception):
    pass


@dataclass
class OrderItem:
    id: int
    name: str
    price: float
    quantity: int


class OrderStatus(str, Enum):
    OPEN = auto()
    PAID = auto()
    SENT = auto()


class Order:
    def __init__(self) -> None:
        self.items: list[OrderItem] = []
        self.status: OrderStatus = OrderStatus.OPEN

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def get_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def send_email(self, total: float, email: str) -> None:
        print(
            f"""
        From: MockShop.com
        To: [{email},]

        Thank you for purchasing in our store.
        We have accepted your payment. Your total was: ${total}.
        Your order will be sent shortly.

        Best regards,
        MockShop.com
        """
        )

    def pay(self, method: str, code: str, email: str) -> None:
        if method == "DEBIT":
            print("Processing debit payment...")
            print(f"Veryfing security code: {code}")
            self.status = OrderStatus.PAID
            self.send_email(total=self.get_total(), email=email)

        elif method == "CREDIT":
            print("Processing credit payment...")
            print(f"Veryfing security code: {code}")
            self.status = OrderStatus.PAID
            self.send_email(total=self.get_total(), email=email)
        else:
            raise InvalidPaymentTypeException(f"{method} payment type is not supported")


if __name__ == "__main__":
    apple = OrderItem(id=1, name="apple", price=3.5, quantity=5)
    orange = OrderItem(id=2, name="orange", price=4, quantity=3)
    order1 = Order()

    order1.add_item(orange)
    print(order1.items)

    order1.pay("DEBIT", code="5584CODE0049", email="test@gmail.com")
