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


class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  # {product_name: quantity}
        self.discount_applied = False
        self.total_price = 0.0

    def add_item(self, product_name, price, quantity):
        if product_name in self.items:
            self.items[product_name]["quantity"] += quantity
        else:
            self.items[product_name] = {"price": price, "quantity": quantity}
        self._calculate_total()

    def remove_item(self, product_name, quantity):
        if product_name in self.items:
            if self.items[product_name]["quantity"] <= quantity:
                del self.items[product_name]
            else:
                self.items[product_name]["quantity"] -= quantity
            self._calculate_total()
        else:
            print(f"{product_name} not in cart.")

    def apply_discount(self, percentage):
        if not self.discount_applied and 0 < percentage <= 100:
            self.total_price *= 1 - percentage / 100
            self.discount_applied = True
            print(f"{percentage}% discound applied.")
        else:
            print("Discount already applied or invalid percentage.")

    def _calculate_total(self):
        current_total = 0.0
        for product_name, details in self.items.items():
            current_total += details["price"] * details["quantity"]
        self.total_price = current_total
        self.discount_applied = False  # Recalculate total, reset discounts status
        print(f"Cart total updated to: {self.total_price}")

    def get_cart_summary(self):
        summary = f"Cart for {self.customer_name}:\n"
        for product_name, details in self.items.items():
            summary += f"- {product_name} (x{details['quantity']}): ${details['price'] * details['quantity']:.2f}\n"
        summary += f"Total: ${self.total_price:.2f}"
        return summary
