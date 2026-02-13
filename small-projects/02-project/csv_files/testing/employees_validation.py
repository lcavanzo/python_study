import csv


def validate_csv(filepath, expected_headers, validation_rules):
    errors = []

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        # 1. Read the header row
        try:
            header = next(reader)
        except StopIteration:
            print(f"{filepath} is empty")
            return

        # 2. Build the Map, (lookup dictionary) for match and ID with the header
        # enumerate gives us pairs like: (0, 'Age'), (1, 'Name')

        header_map = {}
        for index, column_name in enumerate(header):
            header_map[column_name] = index

        if list(header_map.keys()) != expected_headers:
            print(
                f"Header mismatch: expected_headers={expected_headers} - header={list(header_map.keys())}"
            )
            return

        for column_name in validation_rules.keys():
            if column_name not in header_map.keys():
                errors.append(f"Error: Missing Column: {column_name}")
                return

        for row in reader:
            row_is_valid = True
            for column_name, rules_config in validation_rules.items():
                if column_name in header_map.keys():
                    # 1. Get the Generic Value
                    index = header_map[column_name]
                    value = row[index]

                    # 2. Check Required (Generic)
                    if rules_config["required"] is True and value == "":
                        errors.append(f"Error: Missing value for: {column_name}")
                        row_is_valid = False

                    # 3. Check Type (Generic)
                    if rules_config.get("type") == "int":
                        try:
                            int(value)
                        except ValueError:
                            row_is_valid = False
                            errors.append(
                                f"Error: {column_name} contains invalid number '{value}'"
                            )
            if row_is_valid:
                print(f"Data: {row}")
        return errors


rules = {
    "Name": {"required": True, "type": "str"},
    "Age": {"required": True, "type": "int"},
}

expected_headers = ["Name", "Age"]


csv_file = "employees.csv"
validate_csv(csv_file, expected_headers, rules)
