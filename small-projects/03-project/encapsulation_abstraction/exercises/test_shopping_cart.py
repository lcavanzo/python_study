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
        Confirm that public methods (add_item, remove_item) correctly modify the internal state and enforce any validation.
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

    @property
    def customer_name(self):
        return self._customer_name

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
            raise ValueError(f"Item '{product_name}' is not in the cart.")

    def apply_discount(self, percentage):
        if not self._discount_applied and 0 < percentage <= 100:
            self._total_price *= 1 - percentage / 100
            self._discount_applied = True
            # print(f"{percentage}% discound applied.")
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
        # print(f"Cart total updated to: {self.total_price}")

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
    assert sh_cart.customer_name == "Luis"
    assert sh_cart.total_price == 0.0


def test_no_direct_protected_total_price_update():
    sh_cart = ShoppingCart("Diana")
    with pytest.raises(
        AttributeError,
        match="property 'total_price' of 'ShoppingCart' object has no setter",
    ):
        sh_cart.total_price = 20


def test_no_direct_private_items_access():
    sh_cart = ShoppingCart("Mariana")
    with pytest.raises(
        AttributeError,
        match="'ShoppingCart' object has no attribute '__items'",
    ):
        sh_cart.__items


def test_add_items_new_success():
    sh_cart = ShoppingCart("Paulina")
    sh_cart.add_item("Playstation 5", 5000, 1)
    assert (
        sh_cart.get_cart_summary()
        == "Cart for Paulina:\n- Playstation 5 (x1): $5000.00\nTotal: $5000.00"
    )


def test_add_items_update_success():
    sh_cart = ShoppingCart("Lorena")
    sh_cart.add_item("Playstation 5", 5000, 1)
    sh_cart.add_item("Playstation 5", 5000, 1)
    assert (
        sh_cart.get_cart_summary()
        == "Cart for Lorena:\n- Playstation 5 (x2): $10000.00\nTotal: $10000.00"
    )


def test_remove_items_new_success():
    sh_cart = ShoppingCart("Eduardo")
    sh_cart.add_item("Xbox", 3500, 1)
    sh_cart.add_item("Playstation 5", 5000, 1)
    sh_cart.remove_item("Xbox", 1)
    assert (
        sh_cart.get_cart_summary()
        == "Cart for Eduardo:\n- Playstation 5 (x1): $5000.00\nTotal: $5000.00"
    )


def test_private_attribute_access_via_name_mangling():
    sh_cart = ShoppingCart("Frank")
    mangled_salary_attr = f"_{ShoppingCart.__name__}__items"
    # 1. We construct the secret handshake string: "_ShoppintCart__items"
    assert hasattr(sh_cart, mangled_salary_attr)
    # 2. We use 'getattr' to bypass the locked door and grab the money!
    assert getattr(sh_cart, mangled_salary_attr) == {}

    # Test modification via mangled name(again, to show it's posible)
    setattr(
        sh_cart, mangled_salary_attr, {"Playstation 5": {"quantity": 1, "price": 5000}}
    )
    sh_cart._calculate_total()
    assert (
        sh_cart.get_cart_summary()
        == "Cart for Frank:\n- Playstation 5 (x1): $5000.00\nTotal: $5000.00"
    )


if __name__ == "__main__":
    pytest.main()
