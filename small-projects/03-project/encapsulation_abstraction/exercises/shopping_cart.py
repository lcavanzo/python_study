"""
Task:

    Identify which attributes should be protected or private to enforce better encapsulation.
        customer_name: Should it be directly changeable? Or set once?
        items: Should direct modification of this dictionary be allowed?
        discount_applied: Should this be directly accessible/modifiable?
        total_price: This is a calculated value, should it be directly settable?

    Modify the class to use Python's naming conventions (_ or __) to signify protected/private attributes and methods.

    Implement getter methods for any data that should be readable but not directly settable (e.g., total_price).

    Write pytest tests to:
        Verify that internal state (e.g., _total_price, __items) cannot be directly manipulated from outside in ways that bypass logic.
        Confirm that public methods (add_item, remove_item, apply_discount) correctly modify the internal state and enforce any validation.
        Test that the get_cart_summary method returns the correct information.
        Test that the _calculate_total method (now protected) is called correctly by other methods.

"""

import pytest


class ShoppingCart:
    def __init__(self, customer_name):
        self._customer_name = customer_name
        self.__items = {}  # {product_name: quantity}
        self._discount_applied = False
        self._total_price = 0.0

    def add_item(self, product_name, price, quantity):
        if product_name in self.__items:
            self.__items[product_name]["quantity"] += quantity
        else:
            self.__items[product_name] = {"price": price, "quantity": quantity}
        self._calculate_total()

    def remove_item(self, product_name, quantity):
        if product_name in self.__items:
            if self.__items[product_name]["quantity"] <= quantity:
                del self.__items[product_name]
            else:
                self.__items[product_name]["quantity"] -= quantity
            self._calculate_total()
        else:
            print(f"{product_name} not in cart.")

    def apply_discount(self, percentage):
        if not self._discount_applied and 0 < percentage <= 100:
            self._total_price *= 1 - percentage / 100
            self._discount_applied = True
            print(f"{percentage}% discound applied.")
        else:
            print("Discount already applied or invalid percentage.")

    @property
    def total_price(self):
        return self._total_price

    def _calculate_total(self):
        current_total = 0.0
        for product_name, details in self.__items.items():
            current_total += details["price"] * details["quantity"]
        self._total_price = current_total
        self._discount_applied = False  # Recalculate total, reset discounts status
        print(f"Cart total updated to: {self.total_price}")

    def get_cart_summary(self):
        summary = f"Cart for {self._customer_name}:\n"
        for product_name, details in self.__items.items():
            summary += f"- {product_name} (x{details['quantity']}): ${details['price'] * details['quantity']:.2f}\n"
        summary += f"Total: ${self.total_price:.2f}"
        return summary


# Testing behaviour
# shopping = ShoppingCart("Luis")
# shopping.add_item(
#     "playstation 5",
#     5000,
#     1,
# )
# shopping.add_item(
#     "pixel phone",
#     3500,
#     2,
# )
# print()
# print(shopping.get_cart_summary())


# Test file:
def test_shopping_cart_initialization():
    sh_cart = ShoppingCart("Luis")
    assert sh_cart._customer_name == "Luis"
    # Cannot directly access total_price, so we check through get_salary
    assert sh_cart.total_price == 0.0


if __name__ == "__main__":
    pytest.main()
