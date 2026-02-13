"""
You receive configuration lines from a service.
Each line is in the format KEY=VALUE or KEY=VALUE#COMMENT.
Your task is to extract the KEY and VALUE, ignoring any comments and leading/trailing whitespace.

Input Data:
config_line_1 = "DB_HOST=localhost # Primary database host"
config_line_2 = "  APP_PORT=8080 "
config_line_3 = "LOG_LEVEL=INFO"

Desired Output: For config_line_1, you should get KEY='DB_HOST', VALUE='localhost'.
For config_line_2, you should get KEY='APP_PORT', VALUE='8080'. For config_line_3, you should get KEY='LOG_LEVEL', VALUE='INFO'.

Hint: Use split(), strip(), and potentially find() or partition().
"""

import re
import os


def extract_keys_values(filename):
    """
    extract values in the format key=value, value=value
    Args:
        filename(str): The path to the file to read
    Returns:
        dic: extracted values
    """
    content = _read_file(filename)

    # check if file reading failed
    if not content:
        return None

    # regex patterns
    # key_value = re.compile(r'"(\w.*)"')
    key_value = re.compile(r'.* = "\s*(\w+)=(\S+).*"')

    # Store extracted data in a dictionary for clarity
    data = {}
    errors = []

    # Attempt to search and extract data for each pattern
    for line in content.split("\n"):
        if line:
            result = key_value.search(line)
            data[result.group(1)] = result.group(2)
        elif not line:
            continue
        else:
            errors.append(f"Could not find '{line}' in the report file.")
    if errors:
        print("Error(s) during data extraction:")
    for error in errors:
        print(f"- {error}")
        return None  # Return None if essential data is missing

    # Format the report string
    print("--- VALUES ---")
    for key, value in data.items():
        print(f"KEY='{key}', VALUE='{value}'")


def _read_file(filename):
    """
    Reads the entire content of a specified file.
    Args:
        filename (str): The path to the file to read.
    Returns:
        str: The content of the file, or an empty string if an error occurs.
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found at '{filename}'.")
        return ""
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return ""


def _create_input_file(filename):
    """
    Creates a file with predefined server monitoring data.
    Args:
        filename (str): The path where the input file will be created.
    """
    try:
        with open(filename, "w") as f:
            f.write('config_line_1 = "DB_HOST=localhost # Primary database host"\n')
            f.write('config_line_2 = "  APP_PORT=8080 "\n')
            f.write('config_line_3 = "LOG_LEVEL=INFO"\n')
    except Exception as e:
        print(f"Error creating file {filename}: {e} ")
        return None


if __name__ == "__main__":
    config_file = "config_file.txt"
    _create_input_file(config_file)
    extract_keys_values(config_file)
    # # Clean up the created file
    # if os.path.exists(config_file):
    #     os.remove(config_file)
