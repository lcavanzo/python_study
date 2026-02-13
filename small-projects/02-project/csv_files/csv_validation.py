import csv
import re


def validate_csv(filepath, expected_headers, validation_rules):
    """
    Validates a CSV file against a set of expected headers and data validation rules.

    Args:
        filepath (str): Path to the CSV file.
        expected_headers (list): A list of strings representing the expected column headers.
        validation_rules (dict): A dictionary where keys are header names and values are
                                 dictionaries containing validation functions.
                                 Example: {'Age': {'type': int, 'min': 0, 'max': 120}}
                                 Validation functions can be 'type' (Python type),
                                 'regex' (regular expression string), 'required' (bool),
                                 'min' (numeric min value), 'max' (numeric max value),
                                 'choices' (list of allowed values).
    Returns:
        list: A list of error messages found during validation.
    """
    errors = []
    data_rows = []
    header_map = {}  # To map header names to their column index

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            # --- Header Validation ---
            try:
                actual_headers = next(reader)
            except StopIteration:
                errors.append(
                    f"Error: CSV file is empty at {filepath}. No header found."
                )
                return errors  # Cannot proceed without a header

            if len(actual_headers) != len(expected_headers):
                errors.append(
                    f"Header length mismatch. Expected {len(expected_headers)} columns, got {len(actual_headers)}."
                )

            if actual_headers != expected_headers:
                errors.append(
                    f"Header mismatch. Expected {expected_headers}, got {actual_headers}."
                )

            # Build header_map for data validation by column name
            for i, header in enumerate(actual_headers):
                if header in header_map:
                    errors.append(f"Duplicate header found: '{header}' at column {i}.")
                header_map[header] = i

            # --- Row and Data Validation ---
            row_num = 1  # Start from 1 for header, data starts at 2
            for row in reader:
                row_num += 1
                data_rows.append(row)  # Store for potential uniqueness checks later

                if len(row) != len(actual_headers):
                    errors.append(
                        f"Row {row_num}: Column count mismatch. Expected {len(actual_headers)}, got {len(row)}."
                    )
                    continue  # Skip detailed data validation for malformed rows

                for header, rules in validation_rules.items():
                    if header not in header_map:
                        errors.append(
                            f"Row {row_num}: Validation rule for unknown header '{header}'."
                        )
                        continue

                    col_index = header_map[header]
                    if col_index >= len(
                        row
                    ):  # Edge case for inconsistent row lengths already caught
                        continue

                    value = row[col_index].strip()

                    # Required field check
                    if rules.get("required") and not value:
                        errors.append(
                            f"Row {row_num}, Column '{header}': Required field is empty."
                        )
                        continue  # If required and empty, other validations might not make sense

                    if not value and not rules.get(
                        "required"
                    ):  # Allow empty non-required fields to skip further validation
                        continue

                    # Type validation
                    if "type" in rules:
                        expected_type = rules["type"]
                        try:
                            if expected_type == int:
                                int(value)
                            elif expected_type == float:
                                float(value)
                            elif expected_type == bool:
                                if value.lower() not in ["true", "false", "1", "0"]:
                                    errors.append(
                                        f"Row {row_num}, Column '{header}': Invalid boolean value '{value}'."
                                    )
                            # Add other types as needed
                        except ValueError:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Expected type {expected_type.__name__}, got '{value}'."
                            )

                    # Regex validation
                    if "regex" in rules:
                        pattern = rules["regex"]
                        if not re.fullmatch(pattern, value):
                            errors.append(
                                f"Row {row_num}, Column '{header}': Value '{value}' does not match regex '{pattern}'."
                            )

                    # Min/Max value validation (for numeric types)
                    if "min" in rules or "max" in rules:
                        try:
                            num_value = float(
                                value
                            )  # Try float for broader numeric validation
                            if "min" in rules and num_value < rules["min"]:
                                errors.append(
                                    f"Row {row_num}, Column '{header}': Value {num_value} is below minimum {rules['min']}."
                                )
                            if "max" in rules and num_value > rules["max"]:
                                errors.append(
                                    f"Row {row_num}, Column '{header}': Value {num_value} is above maximum {rules['max']}."
                                )
                        except ValueError:
                            # Already caught by type validation, or if field is not numeric
                            pass

                    # Choices (enumerated values) validation
                    if "choices" in rules:
                        allowed_choices = rules["choices"]
                        if value not in allowed_choices:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Value '{value}' is not among allowed choices {allowed_choices}."
                            )

            # --- Uniqueness Validation (after all rows are parsed) ---
            for header, rules in validation_rules.items():
                if "unique" in rules and rules["unique"] and header in header_map:
                    col_index = header_map[header]
                    # values = []  # 1. Create an empty bucket
                    # for row in data_rows:
                    #     # 2. Safety Check: Does this row actually have the column we want?
                    #     # (e.g. if we want column 5, but the row only has 2 items, skip it)
                    #     if col_index < len(row):
                    #         # 3. Extract the specific cell value
                    #         raw_value = row[col_index]
                    #
                    #         # 4. Clean it (remove whitespace)
                    #         clean_value = raw_value.strip()
                    #
                    #         # 5. Add it to our bucket
                    #         values.append(clean_value)
                    values = [
                        row[col_index].strip()
                        for row in data_rows
                        if col_index < len(row)
                    ]
                    seen = set()
                    duplicates = set()
                    for r_idx, val in enumerate(values):
                        if val in seen and val not in duplicates:
                            # Find all row numbers for this duplicate value
                            first_occurrence_row = -1
                            duplicate_rows = []
                            current_row_num = 1  # Header
                            for data_r in range(len(data_rows)):
                                current_row_num += 1
                                if (
                                    col_index < len(data_rows[data_r])
                                    and data_rows[data_r][col_index].strip() == val
                                ):
                                    duplicate_rows.append(current_row_num)

                            errors.append(
                                f"Column '{header}': Duplicate value '{val}' found in rows {', '.join(map(str, duplicate_rows))}."
                            )
                            duplicates.add(val)
                        seen.add(val)

    except FileNotFoundError:
        errors.append(f"Error: File not found at {filepath}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")

    return errors


def report_errors(errors):
    if not errors:
        print("No validation errors found.")
        return

    print(f"\n--- Validation Summary: {len(errors)} Errors ---")
    errors_by_type = {}
    for error_msg in errors:
        # Simple parsing to categorize errors
        if "Header length mismatch" in error_msg:
            error_type = "Header Structure Error"
        elif "Header mismatch" in error_msg:
            error_type = "Header Content Error"
        elif "Column count mismatch" in error_msg:
            error_type = "Row Structure Error"
        elif "Required field is empty" in error_msg:
            error_type = "Missing Required Field"
        elif "Invalid type" in error_msg or "Expected type" in error_msg:
            error_type = "Data Type Error"
        elif "does not match regex" in error_msg:
            error_type = "Regex Pattern Mismatch"
        elif "below minimum" in error_msg or "above maximum" in error_msg:
            error_type = "Value Range Error"
        elif "not among allowed choices" in error_msg:
            error_type = "Invalid Choice"
        elif "Duplicate value" in error_msg:
            error_type = "Duplicate Value Error"
        elif "unknown header" in error_msg:
            error_type = "Configuration Error"
        else:
            error_type = "General Error"

        errors_by_type.setdefault(error_type, []).append(error_msg)

    for error_type, msgs in errors_by_type.items():
        print(f"\n{error_type} ({len(msgs)} instances):")
        for msg in msgs:
            print(f"  - {msg}")


# Define expected headers and validation rules
EXPECTED_HEADERS = ["ID", "Name", "Age", "Email", "Status"]
VALIDATION_RULES = {
    "ID": {"required": True, "type": int, "unique": True, "min": 1},
    "Name": {"required": True, "regex": r"^[A-Za-z\s\-\']+$"},
    "Age": {"required": True, "type": int, "min": 18, "max": 120},
    "Email": {
        "required": True,
        "regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    },
    "Status": {"required": False, "choices": ["Active", "Inactive", "Pending"]},
}

# Create a more complex dummy CSV file for thorough demonstration
complex_sample_data = [
    ["ID", "Name", "Age", "Email", "Status"],
    ["101", "Alice Smith", "30", "alice.s@example.com", "Active"],
    ["102", "Bob Johnson", "25", "bob.j@example.com", "Pending"],
    [
        "103",
        "Charlie Brown",
        "InvalidAge",
        "charlie@example.com",
        "Active",
    ],  # Invalid Age
    ["104", "David Green", "45", "david.g@example", "Active"],  # Invalid Email
    ["105", "Eve Davis", "22", "eve.d@example.com", "Suspended"],  # Invalid Status
    ["106", "Frank White", "50", "frank.w@example.com", "Active"],
    [
        "107",
        "Grace Black",
        "33",
        "grace.b@example.com",
        "Active",
        "Extra",
    ],  # Extra Column
    ["108", "Henry Blue", "28", "henry.b@example.com", "Inactive"],
    ["109", "Ivy Red", "", "ivy.r@example.com", "Active"],  # Missing Age (required)
    ["", "Jack Purple", "40", "jack.p@example.com", "Pending"],  # Missing ID (required)
    [
        "102",
        "Duplicate Bob",
        "26",
        "duplicate.bob@example.com",
        "Inactive",
    ],  # Duplicate ID
    ["110", "Karen Gold", "29", "karen.gold@example.com", "Active"],
    [
        "110",
        "Liam Silver",
        "31",
        "liam.silver@example.com",
        "Inactive",
    ],  # Another Duplicate ID
]

with open("complex_sample_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(complex_sample_data)

print("\n--- Validating 'complex_sample_data.csv' ---")
validation_errors = validate_csv(
    "complex_sample_data.csv", EXPECTED_HEADERS, VALIDATION_RULES
)
report_errors(validation_errors)

# if validation_errors:
#     print(f"Validation completed with {len(validation_errors)} errors:")
#     for error in validation_errors:
#         print(f"- {error}")
# else:
#     print("CSV file is valid!")
#
# # Example with a valid file
# valid_data = [
#     ["ID", "Name", "Age", "Email", "Status"],
#     ["1", "Valid User One", "25", "user1@valid.com", "Active"],
#     ["2", "Valid User Two", "35", "user2@valid.com", "Inactive"],
# ]
# with open("valid_data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(valid_data)
#
# print("\n--- Validating 'valid_data.csv' ---")
# validation_errors_valid = validate_csv(
#     "valid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES
# )
# if validation_errors_valid:
#     print(f"Validation completed with {len(validation_errors_valid)} errors:")
#     for error in validation_errors_valid:
#         print(f"- {error}")
# else:
#     print("CSV file is valid!")
#
# # Example with incorrect headers
# incorrect_headers_data = [
#     ["User_ID", "Full_Name", "AGE", "Email_Address", "Status"],  # Incorrect headers
#     ["1", "Test User", "20", "test@example.com", "Active"],
# ]
# with open("incorrect_headers.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(incorrect_headers_data)
#
# print("\n--- Validating 'incorrect_headers.csv' ---")
# validation_errors_incorrect_headers = validate_csv(
#     "incorrect_headers.csv", EXPECTED_HEADERS, VALIDATION_RULES
# )
# if validation_errors_incorrect_headers:
#     print(
#         f"Validation completed with {len(validation_errors_incorrect_headers)} errors:"
#     )
#     for error in validation_errors_incorrect_headers:
#         print(f"- {error}")
# else:
#     print("CSV file is valid!")
