from dataclasses import dataclass
from enum import Enum, auto
from abc import ABC, abstractmethod, abstractproperty

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# PRINCIPLE : Dependency inversion                            #
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# “Abstractions should not depend on details. Details should  #
# depend on abstraction. High-level modules should not depend #
# on low-level modules. Both should depend on abstractions”   #
#                                                             #
# In other words, make classes depend on abstract classes     #
# rather than non-abstract classes. Abstractions should not   #
# be dependent on low-level methods but both should depend on #
# a third interface.                                          #
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #


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


class Authorizer(ABC):
    @abstractmethod
    def verify_code(self, code: int) -> None:
        pass

    @abstractproperty
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code: int) -> None:
        print(f"Verifying SMS code {code}")
        self.authorized = True

    @property
    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authorizer: Authorizer) -> None:
        self.security_code = security_code
        self.authorizer = authorizer

    def auth_sms(self, code: str) -> None:
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        if not self.authorizer.is_authorized:
            raise Exception("Not authorized")
        print("Processing debit payment...")
        print(f"Veryfing security code: {self.security_code}")
        order.status = OrderStatus.PAID


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("Processing credit payment...")
        print(f"Veryfing security  code: {self.security_code}")
        order.status = OrderStatus.PAID


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str, authorizer: Authorizer) -> None:
        self.email = email
        self.authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.authorizer.is_authorized:
            raise Exception("Not authorized")
        print("Processing paypal payment...")
        print(f"Veryfing email address: {self.email}")
        order.status = OrderStatus.PAID


if __name__ == "__main__":
    apple = OrderItem(id=1, name="apple", price=3.5, quantity=5)
    orange = OrderItem(id=2, name="orange", price=4, quantity=3)

    order = Order()
    authorizer = SMSAuthorizer()
    payment_processor = DebitPaymentProcessor(
        security_code="5584CODE0049", authorizer=authorizer
    )
    email_sender = ConsoleEmailSender()

    authorizer.verify_code(555339)

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
