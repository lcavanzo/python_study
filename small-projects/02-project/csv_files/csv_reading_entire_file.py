"""
For larger files, reading row by row is more memory-efficient than loading the entire file into memory at once.
"""

import csv


def read_csv_for_validation(filepath):
    """
    Reads a CSV file adn return its content as a list of list.
    The first sublist is assumed to be the header
    """
    data = []
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at{filepath}")
        return None
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return None


# Example of usage
# Create a dummy CSV file for demonstration
with open("sample_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Age", "Email"])
    writer.writerow(["1", "Alice", "30", "alice@example.com"])
    writer.writerow(["2", "Bob", "24", "bob@example.com"])
    writer.writerow(
        ["3", "Charlie", "InvalidAge", "charlie@example.com"]
    )  # invalid Age
    writer.writerow(["4", "David", "35", "david.example.com"])  # Invalid email
    writer.writerow(["", "Eve", "28", "eve@example.com"])  # Missing ID
    writer.writerow(
        ["5", "Frank", "22", "frank@example.com", "ExtraColumn"]
    )  # Extra column

csv_content = read_csv_for_validation("sample_data.csv")
if csv_content:
    print("CSV content read succesfully")
    for row in csv_content:
        print(row)
