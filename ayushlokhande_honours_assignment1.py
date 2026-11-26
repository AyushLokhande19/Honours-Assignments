
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def make_payment(self, amount):
        pass


class CardPayment(Payment):

    def __init__(self, card_number, holder, gateway):
        self.card_number = card_number
        self.holder = holder
        self.gateway = gateway

    def show_details(self):
        return f"{self.gateway} Card Payment - ****{self.card_number[-4:]}, Holder: {self.holder}"

    def make_payment(self, amount):
        if amount <= 0:
            return False

        print(f"[{self.gateway}] Card ****{self.card_number[-4:]} charged ${amount}")
        return True


class UPIPayment(Payment):

    def __init__(self, upi_id, gateway):
        self.upi_id = upi_id
        self.gateway = gateway

    def show_details(self):
        return f"{self.gateway} UPI Payment - {self.upi_id}"

    def make_payment(self, amount):
        if amount <= 0:
            return False

        print(f"[{self.gateway}] Payment request of Rs.{amount} sent to {self.upi_id}")
        return True


class PaymentFactory(ABC):

    @abstractmethod
    def create_payment(self, method, **details):
        pass


class RazorpayFactory(PaymentFactory):

    def create_payment(self, method, **details):
        if method == "card":
            return CardPayment(
                details["card_number"],
                details["holder"],
                "Razorpay"
            )

        elif method == "upi":
            return UPIPayment(details["upi_id"], "Razorpay")

        raise ValueError("Unsupported Razorpay payment method")


class StripeFactory(PaymentFactory):

    def create_payment(self, method, **details):
        if method == "card":
            return CardPayment(
                details["card_number"],
                details["holder"],
                "Stripe"
            )

        elif method == "upi":
            return UPIPayment(details["upi_id"], "Stripe")

        raise ValueError("Unsupported Stripe payment method")


class PaymentAggregator(ABC):

    def __init__(self, gateway_name):
        self.gateway_name = gateway_name

    @abstractmethod
    def get_factory(self):
        pass

    def process_payment(self, method, amount, **details):
        factory = self.get_factory()
        payment = factory.create_payment(method, **details)

        print(payment.show_details())
        return payment.make_payment(amount)


class RazorpayAggregator(PaymentAggregator):

    def __init__(self):
        super().__init__("Razorpay")

    def get_factory(self):
        return RazorpayFactory()


class StripeAggregator(PaymentAggregator):

    def __init__(self):
        super().__init__("Stripe")

    def get_factory(self):
        return StripeFactory()


class GatewaySelector:

    gateways = {
        "1": StripeAggregator,
        "2": RazorpayAggregator
    }

    @classmethod
    def select_gateway(cls, choice):
        gateway = cls.gateways.get(choice)

        if gateway is None:
            raise ValueError("Invalid gateway selection")

        return gateway()


def main():

    print("\n===== PAYMENT GATEWAY SYSTEM =====")
    print("1. Stripe")
    print("2. Razorpay")

    gateway_choice = input("Choose payment gateway: ")

    try:
        aggregator = GatewaySelector.select_gateway(gateway_choice)

        print("\nSelect Payment Type:")
        print("1. Card")
        print("2. UPI")

        method_choice = input("Enter your choice: ")

        if method_choice == "1":
            method = "card"
            details = {
                "card_number": input("Enter card number: "),
                "holder": input("Enter card holder name: ")
            }

        elif method_choice == "2":
            method = "upi"
            details = {
                "upi_id": input("Enter UPI ID: ")
            }

        else:
            print("Invalid payment type")
            return

        amount = float(input("Enter payment amount: "))

        print("\n===== PAYMENT PROCESSING =====")

        result = aggregator.process_payment(
            method,
            amount,
            **details
        )

        print("\n===== PAYMENT RESULT =====")
        print("Successful" if result else "Failed")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
