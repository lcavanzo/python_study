import csv


def validate_csv(filepath):
    # The Configuration
    rules = {
        "Name": {"required": True},
        "Age": {"required": True},
    }

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 1. Read the header row
        header = next(reader)

        # 2. Build the Map, (lookup dictionary) for match and ID with the header
        # enumerate gives us pairs like: (0, 'Age'), (1, 'Name')
        header_map = {}
        for index, column_name in enumerate(header):
            header_map[column_name] = index
        print(f"Headers: {header_map}")

        for row in reader:
            for column_name, rules_config in rules.items():
            # row is a list
            name = row[header_map["Name"]]
            age_str = row[header_map["Age"]]
            row_is_valid = True
            if name == "":
                print("Missing Name")
                row_is_valid = False
            try:
                age = int(age_str)
            except ValueError:
                row_is_valid = False
                print(f"Error: Invalid Age '{age_str}'")
            if row_is_valid == True:
                print(f"Data: {name} {age}")


csv_file = "employees.csv"
validate_csv(csv_file)
