import csv


def validate_csv(filepath):
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"Header: {header}")
        for row in reader:
            is_valid = False
            name = row[0]
            age_str = row[1]
            if name == "":
                print("Missing Name")
                is_valid = False
            try:
                age = int(age_str)
                is_valid = True
            except ValueError:
                print(f"Error: Invalid Age '{age_str}'")
            if is_valid:
                print(f"Data: {name} {age}")


csv_file = "employees.csv"
validate_csv(csv_file)
