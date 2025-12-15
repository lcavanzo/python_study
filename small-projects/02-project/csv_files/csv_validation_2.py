import csv
from datetime import datetime


def validate_csv(filepath, expected_headers, validation_rules):
    errors = []
    data_row = []
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                errors.append(
                    f"Error: CSV file is empty at {filepath}. No header found."
                )
                return errors  # Cannot proceed without a header

            if reader.fieldnames is None or reader.fieldnames == "":
                errors.append(f"Error: CSV file error {filepath}. No header found.")

            if reader.fieldnames != expected_headers:
                errors.append(
                    f"Header mismatch. Expected {expected_headers}, got {reader.fieldnames}."
                )
            row_num = 0
            for row in reader:
                row_num += 1
                # print(row)
                data_row.append(row)
                for header, validation_rule in validation_rules.items():
                    value = row.get(header)
                    if value is None:
                        errors.append(f"Row {header} is missing.")
                        continue
                    if validation_rule.get("required") and not value:
                        errors.append(
                            f"Row {row_num}, Column '{header}': Required field is empty."
                        )
                        continue

                    # Type validation
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
                                datetime.strptime(value, format_string)
                        except ValueError:
                            errors.append(
                                f"Row {row_num}, Column '{header}': Expected type '{expected_type}', got '{value}'."
                            )
                    if "custom_validator" in validation_rule:
                        custom_func = validation_rule["custom_validator"]
                        result = custom_func(value)
                        if result is False:
                            errors.append(
                                f"Row {row_num}, Custom validation for {header}: {value} failed"
                            )

    except FileNotFoundError:
        errors.append(f"Error: File not found at {filepath}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")
    return errors


# Define expected headers and validation rules
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

valid_data = [
    ["ID", "Name", "Age", "Email", "HireDate", "Status"],
    ["1", "Valid User One", "25", "user1@valid.com", "2025-02-01", "Active"],
    ["2", "Valid User Two", "35", "user2@valid.com", "2025-10-21", "Inactive"],
]

with open("valid_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(valid_data)


errors = validate_csv("valid_data.csv", EXPECTED_HEADERS, VALIDATION_RULES)
print(errors)
