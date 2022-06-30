from dataclasses import dataclass
from enum import Enum, auto
from abc import ABC, abstractmethod

"""
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# PRINCIPLE : Liskov substitution                             #
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# “Functions that use pointers or references to base classes  #
# must be able to use objects of derived classes without      #
# knowing it”                                                 #
#                                                             #
# In other words, when a class inherits from another class,   #
# the program shouldn't break and you shouldn't need to hack  #
# anything to use the subclass.                               #
# Define constructor arguments to keep inheritance flexible.  #
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
"""


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
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    # --- --- New --- ---
    def __init__(self, code: str) -> None:
        self.code = code

    def pay(self, order: Order):
        print("Processing debit payment...")
        print(f"Veryfing security code: {self.code}")
        order.status = OrderStatus.PAID


class CreditPaymentProcessor(PaymentProcessor):
    # --- --- New --- ---
    def __init__(self, code: str) -> None:
        self.code = code

    def pay(self, order: Order):
        print("Processing credit payment...")
        print(f"Veryfing security  code: {self.code}")
        order.status = OrderStatus.PAID


class PaypalPaymentProcessor(PaymentProcessor):
    # --- --- New --- ---
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, order: Order):
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
