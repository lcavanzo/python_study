"""
Build a Basic Contact List Validator: Create a Python script that validates a CSV file containing contact information.
The CSV should have headers: FirstName, LastName, Phone, Email, City. Implement validation checks for:

    FirstName, LastName: Required, only alphabetical characters and spaces.
    Phone: Optional, must be 10 digits if present (use regex r'^\\d{10}$').
    Email: Required, must be a valid email format (use a regex).
    City: Required, can only be one of a few allowed cities (e.g., "New York", "London", "Paris"). Generate a sample CSV with valid and invalid entries to test your validator.

"""

import csv
import re


def validate_csv(filepath, expected_headers, validation_rules):
    errors = []
    data_rows = []
    compiled_patterns = {}
    cities = []

    for key, rule in validation_rules.items():
        if "regex" in rule:
            compiled_patterns[key] = re.compile(rule["regex"])
        elif "choices" in rule:
            for city in rule["choices"]:
                cities.append(city.lower())

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                errors.append(f"Error: File empty: {filepath}")
                return errors

            if len(expected_headers) != len(reader.fieldnames):
                errors.append(
                    f"Error: Headers Length Mistmatch: expected headers: {len(expected_headers)}, received headers: {len(reader.fieldnames)}"
                )
            if set(expected_headers) != set(reader.fieldnames):
                errors.append(
                    f"Error: Headers Mistmatch: expected headers: {expected_headers}, received headers: {reader.fieldnames}"
                )

            row_number = 0
            for row in reader:
                row_number += 1
                data_rows.append(row)
                for key, validation_rule in validation_rules.items():
                    value = row[key]

                    # Validate required to True
                    if validation_rule["required"] and not value:
                        errors.append(
                            f"Error: Row {row_number}: Column '{key}' is required and must not be empty"
                        )
                        continue

                    # Validate type for each value
                    if validation_rule["required"] is False and not value:
                        continue
                    else:
                        try:
                            expected_type = validation_rule["type"]
                            if expected_type is int:
                                int(value)
                            elif expected_type is float:
                                float(value)
                            elif expected_type is bool:
                                if value.lower() not in ["true", "false", "1", "0"]:
                                    errors.append(
                                        f"Erro: Row {row_number}, Column '{key}': Invalid boolean value '{value}'."
                                    )
                                    continue
                        except ValueError:
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}': Invalid value '{value}'"
                            )
                            continue

                    # Validate Rules
                    if "regex" in validation_rule:
                        pattern = compiled_patterns[key]
                        if not pattern.search(value):
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}', value '{value}' doesn't match the rules."
                            )
                            continue

                    # Validate City
                    if "choices" in validation_rule:
                        if value.lower() not in set(cities):
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}', value '{value}' is not allowed."
                            )
                            continue
    except FileNotFoundError:
        errors.append("File not Found")

    return errors


# Configuration
EXPECTED_HEADERS = ["FirstName", "LastName", "Phone", "Email", "City"]
VALIDATION_RULES = {
    "FirstName": {
        "required": True,
        "type": str,
        "regex": r"^[A-Za-z\s\-\']+$",
    },
    "LastName": {
        "required": True,
        "type": str,
        "regex": r"^[A-Za-z\s\-\']+$",
    },
    "Phone": {
        "required": False,
        "type": str,
        "regex": r"^\d{10}$",
    },
    "Email": {
        "required": True,
        "type": str,
        "regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    },
    "City": {
        "required": True,
        "type": str,
        "choices": [
            "New York",
            "London",
            "Paris",
            "Mexico",
        ],
    },
}

# --- Test Data Creation ---
valid_data = [
    ["FirstName", "LastName", "Phone", "Email", "City"],
    ["Luis", "Cavanzo", "1234567890", "luis@shohoku.com", "Mexico"],
    ["Diana", "Caceres", "9876543210", "diana@ryonan.com", "Paris"],
]

with open("valid_data.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(valid_data)

# Execution
print("--- Starting Validation ---")
errors = validate_csv("valid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)

if errors:
    print("Errors Found:")
    for e in errors:
        print(f"- {e}")
else:
    print("Success! CSV is valid.")

invalid_data = [
    ["FirstName", "LastName", "Phone", "Email", "City"],
    ["Alice", "Kennedy", "5512345678", "alice.smith@example.com", "New York"],
    ["Bob", "Kahn", "4420794601", "bob.jones@testmail.co.uk", "London"],
    ["Charlie", "Brown", "3314567890", "charlie.brown@paris.fr", "Paris"],
    ["David", "Beckam", "5255443322", "david.mx@company.mx", "Mexico"],
    ["Eve", "Patrice", "1234567890", "eve.davis@web.net", "New York"],
    # --- Edge Cases for Testing ---
    ["Frank", "", "9876543210", "frank.white@biz.org", "London"],  # LastName missed
    ["Grace", "Shelby", "12345", "grace.short@example.com", "Paris"],  # Phone too short
    [
        "Henry",
        "Thierry",
        "123456789012",
        "henry.long@example.com",
        "London",
    ],  # Phone too long
    [
        "Ivy",
        "Va",
        "abc1234567",
        "ivy.alpha@example.com",
        "Mexico",
    ],  # Phone contains letters
    [
        "Jack",
        "Sparrow",
        "5512345678",
        "jack.purple@domain",
        "New York",
    ],  # Invalid Email (no TLD)
    [
        "Karen",
        "Zinho",
        "5598765432",
        "karen.gold@example.com",
        "Tokyo",
    ],  # Invalid City (Not in allowed list)
    ["Liam", "Thuram", "5511223344", "", "London"],  # Missing Email
    ["Mike", "Mike", "", "mike.missing@example.com", "Paris"],  # Missing Phone
    ["", "Mo", "5588776655", "nancy.noname@example.com", "Mexico"],  # Missing Name
]

with open("invalid_data.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(invalid_data)

# Execution
print("--- Starting Validation(Invalid data) ---")
errors = validate_csv("invalid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)

if errors:
    print("Errors Found:")
    for e in errors:
        print(f"- {e}")
else:
    print("Success! CSV is valid.")
