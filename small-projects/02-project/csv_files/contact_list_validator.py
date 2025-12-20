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
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                errors.append(f"Error: File empty: {filepath}")
                return errors

            if expected_headers != reader.fieldnames:
                errors.append(
                    f"Error: Headers Mistmatch: expected headers: {expected_headers}, received headers: {reader.fieldnames}"
                )
                return errors

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

                    # Validate type for each value
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

                    except ValueError:
                        errors.append(f"{value}")

                    # Validate FirstName
                    if key == "FirstName":
                        pattern = re.compile(validation_rule["regex"])
                        match = pattern.search(value)
                        if not match:
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}', Name '{value}' doesn't match the rules."
                            )
                            continue

                    # Validate Phone
                    if key == "Phone":
                        if value != "":
                            pattern = re.compile(validation_rule["regex"])
                            match = pattern.search(value)
                            if not match:
                                errors.append(
                                    f"Error: Row {row_number}, Column '{key}', Phone '{value}' doesn't match the rules."
                                )
                        else:
                            continue

                    # Validate email
                    if key == "Email" and (
                        validation_rule["required"] is True and value != ""
                    ):
                        pattern = re.compile(validation_rule["regex"])
                        match = pattern.search(value)
                        if not match:
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}', Email '{value}' doesn't match the rules."
                            )
                            continue

                    # Validate City
                    if key == "City" and (
                        validation_rule["required"] is True and value != ""
                    ):
                        if value.title() not in validation_rule["choices"]:
                            errors.append(
                                f"Error: Row {row_number}, Column '{key}', City '{value}' is not allowed."
                            )
                            continue

    except FileNotFoundError:
        errors.append("File not Found")

    return errors


# Configuration
EXPECTED_HEADERS = ["FirstName", "Phone", "Email", "City"]
VALIDATION_RULES = {
    "FirstName": {
        "required": True,
        "type": str,
        "regex": r"^[A-Za-z\s\-\']+$",
    },
    "Phone": {
        "required": False,
        "type": int,
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
    ["FirstName", "Phone", "Email", "City"],
    ["Luis", "", "luis@shohoku.com", "Mexico"],
    ["Diana", "9876543210", "diana@ryonan.com", "Paris"],
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
