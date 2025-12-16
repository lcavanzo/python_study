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
            for v in reader:
                print(v)

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
        "regex": r"r^\d{10}$",
    },
    "Email": {
        "required": True,
        "type": str,
        "regex": r"asd",
    },
    "City": {
        "required": True,
        "type": str,
        "choices": [
            "New York",
            "London",
            "Paris",
        ],
    },
}

# --- Test Data Creation ---
valid_data = [
    ["FirstName", "Phone", "Email", "City"],
    ["Luis", "1234567890", "luis@shohoku.com", "London"],
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
