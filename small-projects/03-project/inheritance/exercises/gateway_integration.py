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
from unittest import mock


class PaymentGateway:
    """
    Base class to act as a payment gateway
    """

    def process_payment(self, amount):
        """
        method to process a payment
        """
        raise NotImplementedError

    def get_status(self, transaction_id):
        """
        method to get transaction's status
        """
        raise NotImplementedError


class CreditCardGateway(PaymentGateway):
    """
    child class that represents a credit Card payment
    """

    def __init__(self):
        self.credit_limit = 1000

    def process_payment(self, amount):
        """
        Shows the status of a transaction
        """
        if amount > self.credit_limit:
            return f"Successful Payment: ${amount}"
        return "Failed Transaction: Not enough credit"

    def get_status(self, transaction_id):
        """
        child class that show the status of a transaction
        """

        return f"Transaction {transaction_id} - Status:"


class PayPalGateway(PaymentGateway):
    """
    child class that represents a paypal payment
    """

    def process_payment(self, amount):
        """
        Shows the status of a transaction
        """
        return f"Successful Payment: ${amount}"

    def get_status(self, transaction_id):
        """
        child class that show the status of a transaction
        """

        return f"Transaction {transaction_id} - Status:"
