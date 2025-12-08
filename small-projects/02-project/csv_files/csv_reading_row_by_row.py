"""
For larger files, reading row by row is more memory-efficient than loading the entire file into memory at once.

This generator-based approach is ideal for validation, as it allows for immediate processing and reporting of issues without waiting for the entire file to load.
"""

import csv


def process_csv_by_row(filepath):
    """
    Processes a CSV file row by row, yielding each row
    """
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            yield header  # Yield header separately if needed
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except StopIteration:
        print("Error: CSV file is empty")
    except Exception as e:
        print(f"An Error occurred while processing the file: {e}")


print("\nProcessing CSV row by row:")
for i, row in enumerate(process_csv_by_row("sample_data.csv")):
    if i == 0:
        print(f"Header: {row}")
    else:
        print(f"Data row: {row}")


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
