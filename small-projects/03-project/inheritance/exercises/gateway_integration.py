"""
Payment Gateway Integration

Objective: Simulate different payment gateway integrations using inheritance and polymorphism, then test them.

    Create a base class PaymentGateway with methods like process_payment(amount) and get_status(transaction_id). These methods should initially raise NotImplementedError.

    Implement two or more subclasses, such as CreditCardGateway and PayPalGateway.

    Each subclass should provide its own unique implementation for process_payment (e.g., CreditCardGateway might simulate a successful/failed transaction based on amount, PayPalGateway might just confirm a payment). get_status should also return a mock status.

    Write unittest tests to verify that:
        Each gateway subclass correctly processes payments and returns the expected mock transaction IDs or statuses.
        A function designed to use a generic PaymentGateway object can successfully interact with instances of both CreditCardGateway and PayPalGateway polymorphically, demonstrating that the correct process_payment is called for each.

"""

import unittest
import uuid  # Import uuid for generating unique transaction IDs


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds in CreditCardGateway."""

    pass


class PaymentGateway:
    """
    Base class to act as a payment gateway.
    Defines the interface for payment processing and status retrieval.
    """

    def process_payment(self, amount):
        """
        Processes a payment for the given amount.
        Should return a unique transaction ID.
        """
        raise NotImplementedError("Subclasses must implement process_payment method.")

    def get_status(self, transaction_id):
        """
        Retrieves the status of a specific transaction by its ID.
        Should return a string indicating the transaction status.
        """
        raise NotImplementedError("Subclasses must implement get_status method.")


class CreditCardGateway(PaymentGateway):
    """
    Simulates a credit card payment gateway.
    Payments are successful if within the defined credit limit.
    """

    def __init__(self):
        self.credit_limit = 1000
        self._transactions = {}  # Stores transaction_id -> {"amount": ..., "status": ...}

    def process_payment(self, amount):
        """
        Simulates a credit card payment.
        Generates a transaction ID, stores the transaction outcome, and returns the ID.
        Raises InsufficientFundsError if the amount exceeds the credit limit.
        """
        transaction_id = str(uuid.uuid4())
        if amount <= self.credit_limit:
            self._transactions[transaction_id] = {"amount": amount, "status": "SUCCESS"}
            return transaction_id
        else:
            self._transactions[transaction_id] = {"amount": amount, "status": "FAILED"}
            raise InsufficientFundsError("Not enough credit for this transaction.")

    def get_status(self, transaction_id):
        """
        Retrieves the mock status of a credit card transaction by its ID.
        Returns "NOT_FOUND" if the transaction ID does not exist.
        """
        transaction_info = self._transactions.get(transaction_id)
        if transaction_info:
            return (
                f"Transaction {transaction_id} - Status: {transaction_info['status']}"
            )
        return f"Transaction {transaction_id} - Status: NOT_FOUND"


class PayPalGateway(PaymentGateway):
    """
    Simulates a PayPal payment gateway.
    All payments are considered successful in this simulation.
    """

    def __init__(self):
        self._transactions = {}  # Stores transaction_id -> {"amount": ..., "status": ...}

    def process_payment(self, amount):
        """
        Simulates a PayPal payment, always resulting in success.
        Generates a transaction ID, stores the transaction outcome, and returns the ID.
        """
        transaction_id = str(uuid.uuid4())
        self._transactions[transaction_id] = {"amount": amount, "status": "SUCCESS"}
        return transaction_id

    def get_status(self, transaction_id):
        """
        Retrieves the mock status of a PayPal transaction by its ID.
        Returns "NOT_FOUND" if the transaction ID does not exist.
        """
        transaction_info = self._transactions.get(transaction_id)
        if transaction_info:
            return (
                f"Transaction {transaction_id} - Status: {transaction_info['status']}"
            )
        return f"Transaction {transaction_id} - Status: NOT_FOUND"


def handle_payment(gateway_payment_object, amount):
    """
    Processes a payment using the provided generic gateway object.
    This function demonstrates polymorphic behavior.
    """
    return gateway_payment_object.process_payment(amount)


class TestPaymentGateway(unittest.TestCase):
    """
    Test class to test the behavior of the payment gateway classes.
    """

    def test_credit_card_gateway_process_payment_ok(self):
        credit_card_obj = CreditCardGateway()
        transaction_id = credit_card_obj.process_payment(500)
        self.assertIsInstance(transaction_id, str)  # Assert it returns a string ID
        self.assertEqual(
            credit_card_obj.get_status(transaction_id),
            f"Transaction {transaction_id} - Status: SUCCESS",
        )

    def test_credit_card_gateway_process_payment_fails_due_to_funds(self):
        credit_card_obj = CreditCardGateway()
        with self.assertRaises(InsufficientFundsError) as cm:
            credit_card_obj.process_payment(1500)
        self.assertIn("Not enough credit", str(cm.exception))
        # Even though an exception is raised, a transaction ID is still generated
        # We can check its status for "FAILED"
        # However, accessing the ID would require capturing it before the exception
        # For simplicity, we primarily test the exception here.
        # A more complex test might use a try-except to get the ID and then check its status.

    def test_credit_card_gateway_get_status_existing(self):
        credit_card_obj = CreditCardGateway()
        transaction_id = credit_card_obj.process_payment(200)
        actual_status_msg = credit_card_obj.get_status(transaction_id)
        self.assertEqual(
            actual_status_msg, f"Transaction {transaction_id} - Status: SUCCESS"
        )

    def test_credit_card_gateway_get_status_non_existing(self):
        credit_card_obj = CreditCardGateway()
        actual_status_msg = credit_card_obj.get_status("non-existent-id")
        self.assertEqual(
            actual_status_msg, "Transaction non-existent-id - Status: NOT_FOUND"
        )

    def test_paypal_gateway_process_payment_ok(self):
        paypal_payment_obj = PayPalGateway()
        transaction_id = paypal_payment_obj.process_payment(500)
        self.assertIsInstance(transaction_id, str)
        self.assertEqual(
            paypal_payment_obj.get_status(transaction_id),
            f"Transaction {transaction_id} - Status: SUCCESS",
        )

    def test_paypal_gateway_get_status_existing(self):
        paypal_payment_obj = PayPalGateway()
        transaction_id = paypal_payment_obj.process_payment(100)
        actual_status_msg = paypal_payment_obj.get_status(transaction_id)
        self.assertEqual(
            actual_status_msg, f"Transaction {transaction_id} - Status: SUCCESS"
        )

    def test_paypal_gateway_get_status_non_existing(self):
        paypal_payment_obj = PayPalGateway()
        actual_status_msg = paypal_payment_obj.get_status("non-existent-id")
        self.assertEqual(
            actual_status_msg, "Transaction non-existent-id - Status: NOT_FOUND"
        )

    def test_payment_gateway_polymorphic_processing(self):
        """
        Tests that handle_payment can work polymorphically with different gateway types.
        """
        credit_card_obj = CreditCardGateway()
        paypal_obj = PayPalGateway()

        # Process payments polymorphically
        credit_card_transaction_id = handle_payment(credit_card_obj, 300)
        paypal_transaction_id = handle_payment(paypal_obj, 750)

        # Assert correct transaction IDs are returned
        self.assertIsInstance(credit_card_transaction_id, str)
        self.assertIsInstance(paypal_transaction_id, str)

        # Assert correct status is retrieved for each
        self.assertEqual(
            credit_card_obj.get_status(credit_card_transaction_id),
            f"Transaction {credit_card_transaction_id} - Status: SUCCESS",
        )
        self.assertEqual(
            paypal_obj.get_status(paypal_transaction_id),
            f"Transaction {paypal_transaction_id} - Status: SUCCESS",
        )

        # Test polymorphic failure scenario for credit card
        with self.assertRaises(InsufficientFundsError):
            handle_payment(credit_card_obj, 1200)


if __name__ == "__main__":
    unittest.main()
