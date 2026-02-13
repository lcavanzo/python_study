import re
import os


def extract_keys_values(filename):
    """
    Extracts key-value pairs from configuration lines in a file.
    Each line in the file is expected to be in the format:
    variable_name = "KEY=VALUE#COMMENT" or variable_name = "KEY=VALUE"

    Args:
        filename (str): The path to the file to read.

    Returns:
        dict: A dictionary where keys are the extracted KEYs and values are the extracted VALUEs.
              Returns an empty dictionary if no data is found or errors occur.
    """
    content = _read_file(filename)

    if not content:
        return {}  # Return an empty dictionary on file read failure

    extracted_data = {}
    errors = []

    # Regex to extract the quoted string from lines like 'config_line_1 = "..."'
    # This pattern captures whatever is inside the double quotes.
    quoted_string_pattern = re.compile(r'=\s*"(.*?)"')

    for line_num, line in enumerate(
        content.splitlines(), 1
    ):  # Use splitlines() for robustness
        line = line.strip()  # Strip leading/trailing whitespace from the full line

        if not line:
            continue  # Skip empty lines

        match_quoted = quoted_string_pattern.search(line)
        if match_quoted:
            config_string = match_quoted.group(
                1
            )  # This is "KEY=VALUE#COMMENT" or "KEY=VALUE"

            # Now, process the config_string to get KEY and VALUE
            # First, split by '#' to handle comments. Take the first part.
            config_without_comment = config_string.split("#")[0].strip()

            # Now, split by '=' to get KEY and VALUE
            parts = config_without_comment.partition("=")

            if parts[1] == "=":  # Check if '=' was found
                key = parts[0].strip()
                value = parts[2].strip()
                extracted_data[key] = value
            else:
                errors.append(
                    f"Line {line_num}: Invalid config format (no '=' found) in '{config_without_comment}'."
                )
        else:
            errors.append(
                f"Line {line_num}: Could not find a quoted configuration string in '{line}'."
            )

    if errors:
        print("Error(s) during data extraction:")
        for error in errors:
            print(f"- {error}")

    print("\n--- EXTRACTED VALUES ---")
    if extracted_data:
        for key, value in extracted_data.items():
            print(f"KEY='{key}', VALUE='{value}'")
    else:
        print("No key-value pairs were extracted.")

    return extracted_data


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
            f.write(
                'config_line_2 = "  APP_PORT=8080 "\n'
            )  # Note: spaces around the value are handled by strip()
            f.write('config_line_3 = "LOG_LEVEL=INFO"\n')
            f.write(
                'config_line_4 = "INVALID_LINE_NO_EQUALS"\n'
            )  # Example for error handling
            f.write(
                'another_line = "  SOME_KEY=  SOME_VALUE_WITH_SPACES  # Another comment "\n'
            )  # More complex case
    except Exception as e:
        print(f"Error creating file {filename}: {e} ")
        return None


if __name__ == "__main__":
    config_file = "config_file.txt"
    _create_input_file(config_file)
    extracted_values = extract_keys_values(config_file)

    # Optional: You can now work with the extracted_values dictionary
    # print("\nDictionary content:", extracted_values)

    # Clean up the created file
    if os.path.exists(config_file):
        os.remove(config_file)
