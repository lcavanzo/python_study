"""
Develop a basic inventory tracking system for a small shop.

1. Define Schema: Create a JSON Schema for a product object. Each product should have:
    sku: string, required, matches pattern ^[A-Z0-9]{3}-[A-Z0-9]{3}$ (e.g., "ABC-123").
    name: string, required, minLength 5.
    description: string, optional.
    price: number, required, exclusiveMinimum 0.
    quantity_on_hand: integer, required, minimum 0.
    last_updated: string, required, format "date-time".

2. Create Data: Define a list of 2-3 product dictionaries that are valid, and 1-2 product dictionaries that are invalid (e.g., invalid SKU format, negative quantity, missing price).

3. Encode Valid Data: Encode all valid product dictionaries into a single JSON string, formatted with an indentation of 4. Save this string to a file named inventory.json.

4. Load and Validate: Load the inventory.json file. Then, for each product in the loaded list, validate it against your schema. Print a confirmation for each product indicating if it's valid according to the schema.

5. Invalid Data Check: Attempt to validate one of your intentionally invalid product dictionaries directly (without saving/loading). Print the error if it fails.

"""

from jsonschema import Draft7Validator
import json

inventory_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Inventory Schema",
    "description": "Schema For Validating Inventory Objects.",
    "type": "object",
    "properties": {
        "sku": {
            "type": "string",
            "description": "SKU of the product",
            "pattern": "^[A-Z0-9]{3}-[A-Z0-9]{3}$",
        },
        "name": {
            "type": "string",
            "description": "Name of the product",
            "minLength": 5,
        },
        "description": {
            "type": "string",
            "description": "Product description",
        },
        "price": {
            "type": "number",
            "description": "Product Price",
            "exclusiveMinimum": 0,
        },
        "quantity_on_hand": {
            "type": "integer",
            "description": "Available quantity",
            "minimum": 0,
        },
        "last_updated": {
            "type": "string",
            "description": "Timestamp when the product was updated",
            "format": "date-time",
        },
    },
    "required": ["sku", "name", "price", "quantity_on_hand", "last_updated"],
}

VALIDATOR = Draft7Validator(
    schema=inventory_schema, format_checker=Draft7Validator.FORMAT_CHECKER
)


def encode_json(data, filename, indentation):
    """
    Encode data into a json file.

    Return:
        None
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, indent=indentation, fp=file)
    except Exception as e:
        print(f"\nAn unexpected error occured during validation: {e}")


def load_file(filename):
    """
    Load a json file into a python object
    """

    try:
        with open(filename, "r") as f:
            products_list = json.load(f)
        if products_list:
            return products_list
        else:
            return []
    except Exception as e:
        print(f"\nAn unexpected error occured during validation: {e}")


def validate_inventory(product_data, validator):
    """
    Validates an incoming product information against the schema.

    Returns:
        list: A list of error strings. Returns empty list [] if valid.
    """
    errors_found = []
    try:
        errors = sorted(validator.iter_errors(product_data), key=str)

        if errors:
            for error in errors:
                message = f"Error in field {list(error.path)}: {error.message}"
                errors_found.append(message)

    except Exception as e:
        errors_found.append(f"Critical Error: {str(e)}")

    return errors_found


products_inventory = [
    {
        "sku": "ABC-123",
        "name": "Super Widget Pro",
        "description": "A high-performance widget for professionals.",
        "price": 99.99,
        "quantity_on_hand": 150,
        "last_updated": "2025-10-26T10:00:00Z",
    },
    {
        "sku": "XYZ-987",
        "name": "Basic Gadget",
        # Missing description (optional)
        "price": 10.50,
        "quantity_on_hand": 500,
        "last_updated": "2025-10-25T14:30:00Z",
    },
    {  # Invalid SKU (too short)
        "sku": "DEF-45",
        "name": "Compact Charger",
        "price": 25.00,
        "quantity_on_hand": -1,  # Invalid quantity
        "last_updated": "2025-10-26T08:15:00Z",
    },
    {  # Invalid price (not exclusiveMinimum 0)
        "sku": "GHI-789",
        "name": "Mega Monitor",
        "description": "An ultrawide monitor with stunning visuals.",
        "price": -5.00,
        # "quantity_on_hand": 75, # required
        "last_updated": "2025-10-26T11:45:00Z",
    },
    {  # Invalid name (too short), Invalid quantity (string instead of integer)
        "sku": "JKL-010",
        "name": "Pen",
        "price": 1.99,
        "quantity_on_hand": "abc",
        "last_updated": "2025-10-24T17:00:00Z",
    },
]

filename = "inventory.json"

encode_json(products_inventory, filename, 4)

# Testing
loaded_products_inventory = load_file(filename)
if loaded_products_inventory:
    for product in loaded_products_inventory:
        print(f"--- Processing Product {product['name']} ---")
        validation_results = validate_inventory(product, VALIDATOR)

        # Check the size of the list to decide Success vs Failure
        if len(validation_results) == 0:
            print("Status: Valid")
        else:
            print("Status: Invalid")
            print("Details:")
            for msg in validation_results:
                print(f" - {msg}")
        print("\n")
else:
    print("Invalid Data")


# Testing one failed data
print(f"--- Processing Product {products_inventory[4]} ---")
validation_results = validate_inventory(products_inventory[4], VALIDATOR)

# Check the size of the list to decide Success vs Failure
if len(validation_results) == 0:
    print("Status: Valid")
else:
    print("Status: Invalid")
    print("Details:")
    for msg in validation_results:
        print(f" - {msg}")
print("\n")
