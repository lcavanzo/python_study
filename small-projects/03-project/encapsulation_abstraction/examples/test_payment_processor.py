from types import CellType
import pytest
from abc import ABC, abstractmethod


# Re-defining the PaymentProcessor and concrete classes for clarity
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount) -> str:
        pass

    @abstractmethod
    def refund_payment(self, transaction_id, amount) -> bool:
        pass

    def get_supported_currencies(self):
        return ["USD", "EUR", "GBP"]


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"CC_TRANS_{hash(amount)}"

    def refund_payment(self, transaction_id, amount):
        return True


class IncompleteProcessor(PaymentProcessor):
    # This class deliberately does not implement refund_payment
    def process_payment(self, amount):
        return "INCOMPLETE_TRANS"


# Test file
def test_abstract_class_cannot_be_instantiaded():
    with pytest.raises(
        TypeError,
        match="Can't instantiate abstract class PaymentProcessor without an implementation for abstract methods 'process_payment",
    ):
        PaymentProcessor()


def test_concrete_processor_can_be_instantiated():
    cc_processor = CreditCardProcessor()
    assert isinstance(cc_processor, CreditCardProcessor)
    assert isinstance(cc_processor, PaymentProcessor)


def test_incomplete_processor_cannot_be_instantiated():
    with pytest.raises(
        TypeError,
        match="Can't instantiate abstract class IncompleteProcessor without an implementation for abstract method 'refund_payment'",
    ):
        IncompleteProcessor()


def test_credit_card_processor_processes_payment():
    cc_processor = CreditCardProcessor()
    amount = 150.00
    transaction_id = cc_processor.process_payment(amount)
    # In a real test, you might mock external services and check calls
    assert transaction_id.startswith("CC_TRANS_")


def test_credit_card_processor_refunds_payment():
    cc_processor = CreditCardProcessor()
    transaction_id = "CC_TRANS_12345"
    amount = 75.00
    assert cc_processor.refund_payment(transaction_id, amount) is True


if __name__ == "__main__":
    pytest.main()
