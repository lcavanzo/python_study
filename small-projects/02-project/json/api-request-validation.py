import json
from re import T
from typing import Required
from jsonschema import validate, ValidationError, Draft7Validator


# Schema for an API request to create a new product
product_create_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Product Creation Request",
    "description": "Schema for validating product creationn API requests.",
    "type": "object",
    "properties": {
        "name:": {
            "type": "string",
            "description": "Name of the product",
            "minLenght": 3,
        },
        "description": {
            "type": "string",
            "description": "Detailed description of the product",
        },
        "price": {
            "type": "number",
            "description": "Price of the product",
            "exclusiveMinimum": 0,
        },
        "category": {
            "type": "string",
            "description": "category the product belogs to",
            "enum": ["Electronics", "Books", "Apparel", "Home Goods"],
        },
        "tags": {
            "type": "array",
            "description": "List of releveant tags for the product",
            "items": {"type": "string"},
            "uniqueItems": True,
        },
    },
    "required": ["name", "price", "category"],
}

# Simulate an API reqeuest body (valid)
valid_request_body = {
    "name": "Wireless Headphones",
    "description": "High-quality wireless headphones with noise cancellation",
    "price": 199.99,
    "category": "Electronics",
    "tags": ["audio", "bluetooth", "noice-canceling"],
}

# Simulate an API request body (invalid: missing price, invalid category)
invalid_request_body = {
    "name": "Python Book",
    "description": "A comprehensive guide to Python programming.",
    # "price" is missing
    "category": "Software",  # Not in enum
    "tags": ["programming", "python", "book", "python"],  # Duplicate tag
}


def validate_product_request(request_data):
    """
    Validates an incoming product creation request against the schema.
    Returns True if valid, prints errors and returns False otherwise.
    """
    try:
        # Use Draft7Validator to get all errors, not just the first one
        validator = Draft7Validator(product_create_schema)
        errors = sorted(validator.iter_errors(request_data), key=str)
        if errors:
            print(f"\nValidation failed for request: {request_data}")
            for error in errors:
                print(f"- {error.message} (Path: {list(error.path)})")
            else:
                print(f"\nValidation Successful for request: {request_data['name']}")
                return True
    except Exception as e:
        print(f"\nAn unexpected error occured during validation: {e}")
        return False


# Test with valid data
if validate_product_request(valid_request_body):
    print("Proceeding to create product...")
else:
    print("Cannot create product due to validation errors.")

# Test with invalid data
if validate_product_request(invalid_request_body):
    print("Proceeding to create product...")
else:
    print("Cannot create product due to validation errors.")
