"""
Product Inventory CSV Validator: Develop a script to validate a product inventory CSV file.
The file should have headers: ProductID, ProductName, Quantity, Price, Category. Validation requirements:

    ProductID: Required, unique, must be an integer > 0.
    ProductName: Required, string, max length 50 characters.
    Quantity: Required, integer >= 0.
    Price: Required, float > 0.0.
    Category: Required, can only be 'Electronics', 'Books', 'Home Goods', 'Apparel'.
        The script should output all validation errors found, specifying the row number and column for each error.
"""

import csv


def validate_inventory(filepath, expected_headers, validation_rules):
    errors = []
    data_rows = []
    category = []

    for key, validation_rule in validation_rules.items():
        if "Category" in key:
            for c in validation_rule["choices"]:
                category.append(c.lower())

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                errors.append(f"Error: File '{filepath}' is empty")
                return errors

            if len(expected_headers) != len(reader.fieldnames):
                errors.append(
                    f"Error Headers Length Mistmatch: expected headers: {len(expected_headers)}, received headers: {len(reader.fieldnames)}"
                )
                return errors
            if set(expected_headers) != set(reader.fieldnames):
                errors.append(
                    f"Error Headers Mistmatch: expected headers: {expected_headers}, received headers: {reader.fieldnames}"
                )
                return errors
            row_number = 1

            # Handling Unique Values
            ## Example: unique_values= storage = { "ProductID": {1, 2, 3}, "AnotherUniqueCol": {"a", "b"} }
            unique_values_tracker = {}

            # Prefill keys for columns that require uniqueness
            for k, v in validation_rules.items():
                if v.get("unique"):
                    unique_values_tracker[k] = set()

            for row in reader:
                data_rows.append(row)
                row_number += 1
                for key, validation_rule in validation_rules.items():
                    row_value = row[key]

                    # validate required set to true
                    if validation_rule["required"] and not row_value:
                        errors.append(
                            f"Error Row {row_number}: Column '{key}' is required and must not be empty"
                        )
                        continue
                    # validate type value
                    if "type" in validation_rule:
                        expected_type = validation_rule["type"]
                        try:
                            if expected_type is int:
                                int(row_value)
                            if expected_type is float:
                                float(row_value)
                        except ValueError:
                            errors.append(
                                f"Error Row {row_number}: Invalid value '{row_value}', it must be '{expected_type.__name__}'"
                            )
                            continue
                    # Validate category
                    if "choices" in validation_rule:
                        if row_value.lower() not in category:
                            errors.append(
                                f"Error Row {row_number}: Column '{key}', Invalid value '{row_value}', it must be one of '{validation_rule['choices']}'"
                            )
                            continue

                    # Validate min/max value
                    if (
                        "min" in validation_rule or "max" in validation_rule
                    ) and validation_rule["type"] is str:
                        if len(row_value) >= validation_rule["max"]:
                            errors.append(
                                f"Error Row {row_number}: Column {key}, Invalid value '{row_value}', Maximum '{validation_rule['max']}'"
                            )
                            continue
                    elif "min" in validation_rule:
                        if (
                            validation_rule["min"]
                            and round(float(row_value), 2) < validation_rule["min"]
                        ):
                            errors.append(
                                f"Error Row {row_number}: Column {key}, Invalid value '{row_value}', Minimum '{validation_rule['min']}'"
                            )
                            continue
                    elif "max" in validation_rule:
                        if (
                            validation_rule["max"]
                            and round(float(row_value), 2) > validation_rule["max"]
                        ):
                            errors.append(
                                f"Error Row {row_number}: Column {key}, Invalid value '{row_value}', Maximum '{validation_rule['max']}'"
                            )
                        continue
                    

                    print(unique_values_tracker)
                    if "unique" in validation_rule:
                        # check if the value is already in the set for this column
                        if row_value in unique_values_tracker[key]:
                            errors.append(
                                f"Error Row {row_number}: Column '{key}', value '{row_value}' duplicated"
                            )
                        else:
                            unique_values_tracker[key].add(row_value)

    except FileNotFoundError:
        errors.append(f"Error: File '{filepath}' not found")

    return errors


# Configuration
EXPECTED_HEADERS = ["ProductID", "ProductName", "Quantity", "Price", "Category"]
VALIDATION_RULES = {
    "ProductID": {"required": True, "unique": True, "type": int, "min": 1},
    "ProductName": {"required": True, "type": str, "max": 50},
    "Quantity": {"required": True, "type": int, "min": 0},
    "Price": {"required": True, "type": float, "min": 1},
    "Category": {
        "required": True,
        "choices": [
            "Electronics",
            "Books",
            "Home Goods",
            "Apparel",
        ],
    },
}

## Testing
valid_data = [
    ["ProductID", "ProductName", "Quantity", "Price", "Category"],
    ["1", "Laptop", 25, 1200.50, "Electronics"],
    ["2", "Python Book", 50, 35.75, "Books"],
    ["3", "Desk Lamp", 5, 25.00, "Home Goods"],
    ["4", "T-Shirt", 100, 15.99, "Apparel"],
    ["1", "Laptop", 25, 1200.50, "Electronics"],
]
try:
    with open("valid_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(valid_data)
except Exception as e:
    print(f"Error: {e}")


print("--- Starting Validation ---")
errors = validate_inventory("valid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)
if errors:
    print("Errors Found:")
    for e in errors:
        print(f"- {e}")
else:
    print("Success! CSV is valid.")


invalid_data = [
    ["ProductID", "ProductName", "Quantity", "Price", "Category"],
    ["1", "Laptop", 10, 1200.50, "Electronics"],
    ["1", "Keyboard", 15, 75.20, "Electronics"],  # Duplicate ProductID
    ["2", "Python Book", 50, 35.75, "Books"],
    ["", "Monitor", 20, 300.00, "Electronics"],  # Missing ProductID (required)
    ["ABC", "Mouse", 30, 25.50, "Electronics"],  # Invalid ProductID type (not int)
    [0, "Webcam", 5, 40.00, "Electronics"],  # ProductID below min (min: 1)
    [5, "", 5, 50.00, "Books"],  # Missing ProductName (required)
    [
        6,
        "This is an extremely long product name that should definitely exceed the fifty character limit",
        2,
        1000.00,
        "Electronics",
    ],  # ProductName exceeds max length (max: 50)
    [7, "Notebook", None, 60.00, "Books"],  # Missing Quantity (required)
    [8, "Pens", -1, 10.00, "Home Goods"],  # Quantity below min (min: 0)
    [9, "Chair", 10, None, "Home Goods"],  # Missing Price (required)
    [10, "Headphones", 20, 0.50, "Electronics"],  # Price below min (min: 1)
    [
        11,
        "Coffee Maker",
        8,
        75.00,
        "Kitchen Appliances",
    ],  # Invalid Category (not in choices)
]

try:
    with open("invalid_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(invalid_data)
except Exception as e:
    print(f"Error: {e}")

print("--- Starting Validation(invalida data) ---")
errors = validate_inventory("invalid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)
if errors:
    print("Errors Found:")
    for e in errors:
        print(f"- {e}")
else:
    print("Success! CSV is valid.")
