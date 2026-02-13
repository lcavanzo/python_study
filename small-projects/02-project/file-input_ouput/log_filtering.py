"""
Task: Create a Python script that reads a webserver_access.log file.
Filter out all lines that indicate a successful request (HTTP status code 200) and write the remaining lines (errors, redirects, etc.) to a new file called webserver_errors.log.
After creating webserver_errors.log, calculate its SHA256 hash and save it to webserver_errors.log.sha256.

webserver-file:
192.168.1.10 - - [27/Oct/2023:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.11 - - [27/Oct/2023:10:00:05 +0000] "GET /admin HTTP/1.1" 401 567
192.168.1.12 - - [27/Oct/2023:10:00:10 +0000] "POST /api/data HTTP/1.1" 500 89
192.168.1.10 - - [27/Oct/2023:10:00:15 +0000] "GET /images/logo.png HTTP/1.1" 200 456
192.168.1.13 - - [27/Oct/2023:10:00:20 +0000] "GET /nonexistent HTTP/1.1" 404 100

# TODO:
- [x] - Create a function to read the webserver.log file
- [x] - Filter out 2xx requests
- [x] - Send non-2xx to a new errors.log file
- [X] - Calculate SHA256 for error.log file
- [X] - Save SHA256 value into error.log.sha256 file
"""

import re
import hashlib
import os  # For cleanup


def read_file(filepath):
    """
    Reads the entire content of a file.
    Returns content as a string, or None if an error occurs.
    """
    content = None
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Warning: file not found: {filepath}")
    except IOError as e:
        print(f"Error reading log file {filepath}: {e}")
    return content


def verify_and_process_log_file(filepath, error_filepath):
    """
    Reads the main log file, filters out 2xx requests, writes non-2xx to an error file,
    and calculates/saves the SHA256 hash of the error file.
    """
    print(f"--- Processing log file: {filepath} ---")
    log_content = read_file(filepath)

    if log_content:
        filter_errors(log_content, error_filepath)
    else:
        print("No content found in primary log file, no errors to process.")
        return  # Exit if nothing to process

    print(f"\n--- Calculating SHA256 hash for error log: {error_filepath} ---")
    calculated_hash = calculate_file_hash(error_filepath)

    if calculated_hash:
        hash_filename = f"{error_filepath}.sha256"
        try:
            with open(hash_filename, "w") as h_file:
                h_file.write(calculated_hash)
                # h_file.write("a")  # testing an error
            print(f"--- SHA256 hash saved to: {hash_filename} ---")
        except IOError as e:
            print(f"Error saving hash to file {hash_filename}: {e}")
    else:
        print(
            f"Could not calculate hash for {error_filepath}. Skipping hash file creation."
        )

    print("\n\n---Validating hash---")
    hash_filename_content = read_file(f"{error_filepath}.sha256")
    if calculated_hash == hash_filename_content:
        print("Both hashes are equal")
    else:
        print("---Incorrect Hash---")
        return None


def calculate_file_hash(filepath, algorithm="sha256", block_size=65536):
    """
    Calculates the hash of a file using the specified algorithm.
    Reads the file in chunks for memory efficiency.
    Returns the hexadecimal hash string, or None if an error occurs.
    """
    try:
        hasher = None
        if algorithm == "sha256":
            hasher = hashlib.sha256()
        elif algorithm == "md5":
            hasher = hashlib.md5()
        else:
            print(
                f"Error: Unsupported hashing algorithm '{algorithm}'. Choose 'md5' or 'sha256'."
            )
            return None

        with open(filepath, "rb") as f:  # Open in binary mode for hashing
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found for hashing: {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath} for hashing: {e}")
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred during hash calculation for {filepath}: {e}"
        )
    return None


def filter_errors(log_content, error_filepath):
    """
    Filters lines from log_content that do not have a 2xx HTTP status code
    and writes them to the specified error_filepath.
    """
    error_messages = []
    # Using log_content.splitlines() removes newline characters from each line.
    # We must add them back when writing to the file.
    for line in log_content.splitlines():
        columns = line.split()
        status_code_str = columns[-2]
        # Check if the status code string starts with anything other than '2'
        # This filters out all 2xx codes (200, 201, 299, etc.)
        if re.match(r"^(?!2\d\d)", status_code_str):
            error_messages.append(line)

    try:
        with open(error_filepath, "w") as f:
            for error in error_messages:
                f.write(error + "\n")  # Add newline character back
        print(f"--- Non-2xx requests written to: {error_filepath} ---")
    except IOError as e:
        print(f"Error writing to error log file {error_filepath}: {e}")


# --- Demonstration ---
webserver_file = "webserver_access.log"
webserver_errors = "webserver_errors.log"
webserver_errors_hash_file = f"{webserver_errors}.sha256"

# Create sample file
print("--- Creating sample webserver_access.log ---")
with open(webserver_file, "w") as sample_f:
    sample_f.write(
        '192.168.1.10 - - [27/Oct/2023:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1234\n'
    )
    sample_f.write(
        '192.168.1.11 - - [27/Oct/2023:10:00:05 +0000] "GET /admin HTTP/1.1" 401 567\n'
    )
    sample_f.write(
        '192.168.1.12 - - [27/Oct/2023:10:00:10 +0000] "POST /api/data HTTP/1.1" 500 89\n'
    )
    sample_f.write(
        '192.168.1.10 - - [27/Oct/2023:10:00:15 +0000] "GET /images/logo.png HTTP/1.1" 200 456\n'
    )
    sample_f.write(
        '192.168.1.13 - - [27/Oct/2023:10:00:20 +0000] "GET /nonexistent HTTP/1.1" 404 100\n'
    )
    sample_f.write(
        '192.168.1.200 - - [27/Oct/2023:10:00:20 +0000] "GET /another_success HTTP/1.1" 299 100\n'
    )
    sample_f.write(
        '192.168.1.201 - - [27/Oct/2023:10:00:25 +0000] "GET /redirect HTTP/1.1" 302 0\n'
    )
    sample_f.write(
        '192.168.1.202 - - [27/Oct/2023:10:00:30 +0000] "GET /malformed HTTP/1.1" 503\n'  # Malformed line for testing
    )

verify_and_process_log_file(webserver_file, webserver_errors)

# --- Cleanup (Optional, but good practice for repeatable runs) ---
print("\n--- Cleaning up generated files ---")
try:
    if os.path.exists(webserver_file):
        os.remove(webserver_file)
        print(f"Removed: {webserver_file}")
    if os.path.exists(webserver_errors):
        os.remove(webserver_errors)
        print(f"Removed: {webserver_errors}")
    if os.path.exists(webserver_errors_hash_file):
        os.remove(webserver_errors_hash_file)
        print(f"Removed: {webserver_errors_hash_file}")
except OSError as e:
    print(f"Error during cleanup: {e}")
