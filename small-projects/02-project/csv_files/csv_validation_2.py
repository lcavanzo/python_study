import csv
from datetime import datetime
import re


def validate_csv(filepath, expected_headers, validation_rules):
    errors = []
    data_row = []  # Memory bank to store all rows for uniqueness checks

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # --- 1. Header Validation ---
            # Check if file is completely empty (no fieldnames)
            if not reader.fieldnames:
                errors.append(
                    f"Error: CSV file is empty at {filepath}. No header found."
                )
                return errors

            # Check if headers match expectations
            if reader.fieldnames != expected_headers:
                errors.append(
                    f"Header mismatch. Expected {expected_headers}, got {reader.fieldnames}."
                )

            # --- 2. Row-by-Row Validation ---
            row_num = 1  # Start at 1 (Header is row 1)
            for row in reader:
                row_num += 1
                data_row.append(row)  # Save row to memory bank

                for header, validation_rule in validation_rules.items():
                    # Get value safely (handle missing columns in specific rows)
                    value = row.get(header)

                    # Check if column is missing entirely from this row
                    if value is None:
                        errors.append(f"Row {row_num}: Column '{header}' is missing.")
                        continue

                    value = value.strip()  # Clean whitespace

                    # Check 'Required' Rule
                    if validation_rule.get("required") and not value:
                        errors.append(
                            f"Row {row_num}, Column '{header}': Required field is empty."
                        )
                        continue  # Stop checking this cell if it's empty

                    # Skip other checks if empty and not required
                    if not value and not validation_rule.get("required"):
                        continue

                    # --- Type Validation ---
                    if "type" in validation_rule:
                        expected_type = validation_rule["type"]
                        try:
                            if expected_type is int:
                                int(value)
                            elif expected_type is float:
                                float(value)
                            elif expected_type is bool:
                                if value.lower() not in ["true", "false", "1", "0"]:
                                    errors.append(
                                        f"Row {row_num}, Column '{header}': Invalid boolean value '{value}'."
                                    )
                            elif expected_type == "date":
                                format_string = validation_rule["format"]
                                # Just TEST the parsing, do not overwrite 'value' with the object
                                datetime.strptime(value, format_string)

                        except ValueError:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Expected type '{expected_type}', got '{value}'."
                            )

                    # --- Custom Function Validation ---
                    if "custom_validator" in validation_rule:
                        custom_func = validation_rule["custom_validator"]
                        result = custom_func(value)
                        if result is False:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Custom validation failed for value '{value}'."
                            )

                    # --- Regex Validation ---
                    if "regex" in validation_rule:
                        pattern = validation_rule["regex"]
                        if not re.fullmatch(pattern, value):
                            errors.append(
                                f"Row {row_num}, Column '{header}': Value '{value}' does not match pattern."
                            )

                    # --- Min/Max Validation ---
                    if "min" in validation_rule or "max" in validation_rule:
                        try:
                            num_value = float(value)
                            if (
                                "min" in validation_rule
                                and num_value < validation_rule["min"]
                            ):
                                errors.append(
                                    f"Row {row_num}, Column '{header}': Value {num_value} is below minimum."
                                )
                            if (
                                "max" in validation_rule
                                and num_value > validation_rule["max"]
                            ):
                                errors.append(
                                    f"Row {row_num}, Column '{header}': Value {num_value} is above maximum."
                                )
                        except ValueError:
                            pass  # Already caught by type check

                    # --- Choices Validation ---
                    if "choices" in validation_rule:
                        allowed_choices = validation_rule["choices"]
                        if value not in allowed_choices:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Value '{value}' is not valid choice."
                            )

            # --- 3. Uniqueness Validation (Post-Processing) ---
            # This runs once after reading the whole file
            for header, rules in validation_rules.items():
                # Only run if rule has 'unique': True AND the header actually exists
                if (
                    rules.get("unique")
                    and reader.fieldnames
                    and header in reader.fieldnames
                ):
                    # Extract the list of ALL values for this column
                    values = [r.get(header, "").strip() for r in data_row]

                    seen = set()
                    duplicates = set()

                    # Iterate through every single value (apple) in the list (bucket)
                    for val in values:
                        if val in seen and val not in duplicates:
                            # Start Search Party: Find row numbers for this duplicate
                            duplicate_rows = []

                            # Scan memory bank again
                            for i, r in enumerate(data_row):
                                # i starts at 0, which corresponds to Row 2 in CSV (Row 1 is Header)
                                human_row_num = i + 2
                                val_in_row = r.get(header, "").strip()

                                if val_in_row == val:
                                    duplicate_rows.append(str(human_row_num))

                            errors.append(
                                f"Column '{header}': Duplicate value '{val}' found in rows {', '.join(duplicate_rows)}."
                            )
                            duplicates.add(val)
                        seen.add(val)

    except FileNotFoundError:
        errors.append(f"Error: File not found at {filepath}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")

    return errors


# --- Configuration ---
EXPECTED_HEADERS = ["ID", "Name", "Age", "Email", "HireDate", "Status"]

VALIDATION_RULES = {
    "ID": {"required": True, "type": int, "unique": True, "min": 1},
    "Name": {"required": True, "regex": r"^[A-Za-z\s\-\']+$"},
    "Age": {"required": True, "type": int, "min": 18, "max": 120},
    "Email": {
        "required": True,
        "regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "custom_validator": lambda x: x.endswith(".com"),
    },
    "HireDate": {"required": True, "type": "date", "format": "%Y-%m-%d"},
    "Status": {"required": False, "choices": ["Active", "Inactive", "Pending"]},
}

# --- Test Data Creation ---
valid_data = [
    ["ID", "Name", "Age", "Email", "HireDate", "Status"],
    ["1", "Valid User One", "25", "user1@valid.com", "2025-02-01", "Active"],
    ["2", "Valid User Two", "35", "user2@valid.com", "2025-10-21", "Inactive"],
    [
        "1",
        "Duplicate ID User",
        "35",
        "dup@valid.com",
        "2025-10-22",
        "Inactive",
    ],  # Duplicate ID Test
    [
        "4",
        "Bad Date User",
        "35",
        "bad@valid.com",
        "2025/10/22",
        "Inactive",
    ],  # Bad Date Test
]

with open("valid_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(valid_data)

# --- Execution ---
print("--- Starting Validation ---")
errors = validate_csv("valid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)

if errors:
    print("Errors Found:")
    for e in errors:
        print(f"- {e}")
else:
    print("Success! CSV is valid.")
