from abc import ABC, abstractmethod


class PaymentProcessor(ABC):  # Inherit from ABC makes this and Abtract Base Class
    @abstractmethod
    def process_payment(self, amount) -> str:
        """
        Processes a payment of the givem amount
        """
        pass

    @abstractmethod
    def refund_payment(self, transaction_id, amount) -> bool:
        """
        Refunds a payment for a given transaction ID and amount
        """
        pass

    def get_supported_currencies(self):  # Concrete method, not abstract
        return ["USD", "EUR", "GBP"]


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}.")
        # Complex logi for interacting with credit card API's
        return f"CC_TRANS_{hash(amount)}"  # Return a mock transaction ID

    def refund_payment(self, transaction_id, amount):
        print(f"Initiating credit card refund for {transaction_id} of ${amount}.")
        # Complex logic for credit card refund API's
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Paypal payment of ${amount}")
        # Complex logi for interacting with Paypal API's
        return f"PP_TRANS_{hash(amount)}"  # Return a mock transaction ID

    def refund_payment(self, transaction_id, amount):
        print(f"Initiating Paypal refund for {transaction_id} of ${amount}.")
        # Complex logic for Paypal refund API's
        return True


# Attempting to instantiate an abstract class directly (will raise TypeError)
try:
    processor = PaymentProcessor()
except TypeError as e:
    print(f"Erro: {e}")

# Instantiate concrete processors
cc_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()

# Interact with processors through the abstract interface
print(f"Supported currencies: {cc_processor.get_supported_currencies()}")
cc_trans_id = cc_processor.process_payment(100.00)
cc_processor.refund_payment(cc_trans_id, 50.00)

print(f"Supported currencies: {paypal_processor.get_supported_currencies()}")
pp_trans_id = paypal_processor.process_payment(250.50)
paypal_processor.refund_payment(pp_trans_id, 100.00)
