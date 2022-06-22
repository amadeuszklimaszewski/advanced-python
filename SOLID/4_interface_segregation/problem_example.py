from dataclasses import dataclass
from enum import Enum, auto
from abc import ABC, abstractmethod


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


class EmailSender(ABC):
    @abstractmethod
    def send_email(self, sender: str, receiver: str, subject: str, body: str) -> None:
        pass


class ConsoleEmailSender(EmailSender):
    def send_email(self, sender: str, receiver: str, subject: str, body: str) -> None:
        print(
            f"""
        From: {sender}
        To: [{receiver},]
        Subject: {subject}

        {body}
        """
        )


class PaymentProcessor(ABC):
    def auth_sms(self, code: str) -> None:
        pass

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code: str) -> None:
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment...")
        print(f"Veryfing security code: {self.security_code}")
        order.status = OrderStatus.PAID


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def auth_sms(self, code: str) -> None:
        raise Exception("Credit card payments don't support SMS code authorization.")

    def pay(self, order: Order) -> None:
        print("Processing credit payment...")
        print(f"Veryfing security  code: {self.security_code}")
        order.status = OrderStatus.PAID


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str) -> None:
        self.email = email
        self.verified = False

    def auth_sms(self, code: str) -> None:
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment...")
        print(f"Veryfing email address: {self.email}")
        order.status = OrderStatus.PAID


if __name__ == "__main__":
    apple = OrderItem(id=1, name="apple", price=3.5, quantity=5)
    orange = OrderItem(id=2, name="orange", price=4, quantity=3)

    order = Order()
    payment_processor = DebitPaymentProcessor(code="5584CODE0049")
    email_sender = ConsoleEmailSender()

    order.add_item(orange)
    payment_processor.pay(order=order)
    email_info = {
        "sender": "MockShop.com",
        "receiver": "test@gmail.com",
        "subject": "Order confirmation",
        "body": f"""
        Thank you for purchasing in our store.
        We have accepted your payment. Your total was: ${order.get_total()}.
        Your order will be sent shortly.

        Best regards,
        MockShop.com""",
    }
    email_sender.send_email(**email_info)
