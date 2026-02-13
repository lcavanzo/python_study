import hashlib
import re


def calculate_file_hash(filepath, algorithm="sha256", block_size=65536):
    """
    Calculates the hash of a file
    """
    try:
        hasher = hashlib.sha256() if algorithm == "sha256" else hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None


def process_and_verify_log(log_filepath, expected_hash_filepath):
    """
    Reads a log file, extracts error messages and verifies its integriry
    """
    print(f"---Processing and Verifying Log File: {log_filepath} ---")
    # Step1: Read the expected hash from a separate, trusted file
    expected_hash = None
    try:
        with open(expected_hash_filepath, "r") as h_file:
            expected_hash = h_file.read().strip()
        print(f"Loaded expected hash: {expected_hash}")
    except FileNotFoundError:
        print(
            f"Warning: Expected hash file '{expected_hash_filepath}' not found. Cannot verify integrity."
        )
        # Proceed with log processing but without integrity check
    except IOError as e:
        print(f"Error reading expected hash file: {e}")
        # Proceed with log processing but without integrity check

    # Step2: Calcualte the current has of the log file
    current_hash = calculate_file_hash(log_filepath, "sha256")

    # Step3: Perform integrity check ( if expected hash was available)
    if expected_hash and current_hash:
        if current_hash == expected_hash:
            print("LOG INTEGRITY CHECK PASSED: log file content matches expected.")
        else:
            print(
                "!!!! LOG INTEGRITY CHECK FAILED: Log file has been altered or corrupted."
            )
            print(f"  Expected: {expected_hash}")
            print(f"  Current:  {current_hash}")
            # In a real SRE scenario, this would trigger an alert!
            return  # Stop processing if integrity is compromised for security

    elif not expected_hash and current_hash:
        print(f"No expected hash to compare against. Current hash: {current_hash}")
        # In a real scenario, you might want to save this as the new trsuted hash
        with open(expected_hash_filepath, "w") as h_file:
            h_file.write(current_hash)
        print(f"Saved current hash as new baseline to {expected_hash_filepath}")
    # Step4: process the log file content
    error_messages = []
    try:
        with open(log_filepath, "r") as log_file:
            for line_num, line in enumerate(log_file, 1):
                # Simple regex to find lines containing "ERROR" or "CRITICAL"
                if re.search(r"ERROR|CRITICAL", line, re.IGNORECASE):
                    error_messages.append(f"Line {line_num}: {line.strip()}")
        if error_messages:
            print("\nFound the following critical log entries")
            for msg in error_messages:
                print(f"- {msg}")
        else:
            print("\nNo critical log entries found.")
    except FileNotFoundError:
        print(f"Error: Log file '{log_filepath}' not found for processing.")
    except IOError as e:
        print(f"Error reading log file '{log_filepath}': {e}")


# --- Demostration ---
service_log = "service_runtime.log"
log_hash_file = "service_runtime.log.sha256"

# Create a sample log file
with open(service_log, "w") as f:
    f.write("2025-10-27 11:00:01 INFO: Service started.\n")
    f.write("2025-10-27 11:00:05 DEBUG: Initializing components.\n")
    f.write("2025-10-27 11:00:10 WARNING: Disk usage 80%.\n")
    f.write("2025-10-27 11:00:15 ERROR: Database connection failed.\n")
    f.write("2025-10-27 11:00:20 INFO: Retrying database connection...\n")

# Run the processor for the first time (no hash file exists, so it will create one)
process_and_verify_log(service_log, log_hash_file)

print("\n--- Simulating normal operation (no change to log content) ---")
process_and_verify_log(service_log, log_hash_file)

# Simulate an external modification to the log file(e.g. someone editing it)
print("\n--- Simulating log file modification ---")
with open(service_log, "a") as f:  # Append a new line to simulate more loggin
    f.write(
        "2025-10-27 11:00:25 CRITICAL: Out of memory error! Service shutting down.\n"
    )
with open(service_log, "r+") as f:  # Now try to modify an existing line
    lines = f.readlines()
    if len(lines) > 2:
        lines[2] = (
            "2025-10-27 11:00:10 WARNING: Disk usage 99% (CRITICAL!).\n"  # Altered existing line
        )
    f.seek(0)  # Go to start of file
    f.writelines(lines)  # Write all lines back
    f.truncate()  # Crucial to remove any lefover characters if new lines are shorter

process_and_verify_log(service_log, log_hash_file)
