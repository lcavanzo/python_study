"""
Task: Write a function audit_config_file(filepath, baseline_hash_file) that takes a configuration file path and a path to a file containing its baseline SHA256 hash. The function should:

- [x] - Read the baseline hash. If the baseline_hash_file does not exist, it should calculate the current hash of filepath, save it to baseline_hash_file, and report that a new baseline was established.

- [X] - If the baseline_hash_file exists, compare the current hash of filepath with the baseline.

- [X] - Print a clear message indicating whether the configuration file's integrity passed or failed the audit.

- [X] - Handle FileNotFoundError for both the config file and the hash file gracefully.

Hint: Adapt the calculate_file_hash and verify_file_integrity functions from the lesson.


"""

import hashlib
import json
import os


def audit_config_file(filepath, baseline_hash_file):
    """
    Audits the integrity of a configuration file against a baseline SHA256 hash.

    Args:
        filepath (str): The path to the configuration file to audit.
        baseline_hash_file (str): The path to the file storing the baseline SHA256 hash.
                                  If it doesn't exist, a new baseline will be established.
    """
    # 1. Check if the configuration file itself exists
    if not os.path.exists(filepath):
        print(f"Audit Failed: Configuration file '{filepath}' not found.")
        return

    # 2. Calculate the current hash of the configuration file
    current_hash = calculate_hash(filepath)
    if current_hash is None:
        print(
            f"Audit Failed: Could not calculate hash for configuration file '{filepath}'."
        )
        return

    # 3. Attempt to read the baseline hash
    baseline_hash_content = read_file_content(baseline_hash_file)

    if baseline_hash_content is None:
        # Case: Baseline hash file does not exist or could not be read.
        # Establish a new baseline.
        print(f"--- Establishing New Baseline for '{filepath}' ---")
        try:
            with open(baseline_hash_file, "w") as f:
                f.write(current_hash)
            print(f"New baseline hash saved to '{baseline_hash_file}'.")
            print(
                f"Integrity check for '{filepath}' initialised. No existing baseline to compare."
            )
        except IOError as e:
            print(
                f"Error: Could not write new baseline hash to '{baseline_hash_file}': {e}"
            )
        except Exception as e:
            print(f"An unexpected error occurred while writing baseline: {e}")
    else:
        # Case: Baseline hash file exists, compare current hash with baseline.
        if current_hash == baseline_hash_content:
            print(f"--- File Integrity Passed for '{filepath}' ---")
        else:
            print(f"--- File Integrity FAILED for '{filepath}' ---")
            print(f"  Configuration File: '{filepath}'")
            print(f"  Current Hash:   {current_hash}")
            print(f"  Baseline Hash:  {baseline_hash_content}")


def calculate_hash(filepath, algorithm="sha256", block_size=65536):
    """
    Calcualte hash for a file.
    Args:
        filepath: path of the file
        algorithm: sha256 by default
        block_size: size of each shard for hashing, 65536 by default
    return:
        hash: hash for the file
    """
    if algorithm == "sha256":
        hasher = hashlib.sha256()
    elif algorithm == "md5":
        hasher = hashlib.md5()
    else:
        return None
    try:
        with open(filepath, "rb") as f:
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
    except (FileNotFoundError, IOError) as e:
        return None
    except Exception as e:
        print(f"An unexpected error occureed: {e}")
        return None
    return hasher.hexdigest()


def read_file_content(filepath, mode="r"):
    """
    Read a file's entire content.
    Args:
        filepath: path of the file
        mode(optional): open mode, read by default
    return:
        content: content of the file as a string, or None if an error occurred (e.g., FileNotFoundError).
    """
    try:
        with open(filepath, mode) as f:
            content = f.read()
    except (FileNotFoundError, IOError) as e:
        return None
    except Exception as e:
        print(f"An unexpected error occurred during file read '{filepath}': {e}")
        return None
    return content


# - Demonstation
print("--- Starting Audit Demonstration ---")

audit_file = "audit-config.json"
audit_file_hash = f"{audit_file}.sha256"

# Ensure old hash file is removed for first run test
if os.path.exists(audit_file_hash):
    os.remove(audit_file_hash)

# Dummy audit config file
audit_config_data = {
    "general": {"report_file": "audit_report.log", "default_hash_algorithm": "sha256"},
    "files_to_monitor": [
        {
            "name": "Webserver Error Log",
            "path": "/var/log/webserver_errors.log",
            "expected_hash_file": "/var/log/webserver_errors.log.sha256",
        },
        {
            "name": "System Hosts File",
            "path": "/etc/hosts",
            "expected_hash_file": "/etc/hosts.sha256",
        },
    ],
}

# Create the dummy config file
with open(audit_file, "w") as f:
    json.dump(audit_config_data, f)

print("\n--- First Audit Run (Establishing Baseline) ---")
audit_config_file(audit_file, audit_file_hash)

print("\n--- Second Audit Run (Verifying against Baseline) ---")
audit_config_file(audit_file, audit_file_hash)

# Modify the config file to trigger a failure
print("\n--- Modifying Config File ---")
audit_config_data["general"]["report_file"] = "audit_report_v2.log"
with open(audit_file, "w") as f:
    json.dump(audit_config_data, f, indent=4)

print("\n--- Third Audit Run (Integrity FAILED) ---")
audit_config_file(audit_file, audit_file_hash)

# Test with a non-existent config file
print("\n--- Audit Run with Non-Existent Config File ---")
audit_config_file("non-existent-config.json", "non-existent-config.json.sha256")

# Clean up created files
print("\n--- Cleaning up ---")
if os.path.exists(audit_file):
    os.remove(audit_file)
if os.path.exists(audit_file_hash):
    os.remove(audit_file_hash)
print("--- Demonstration Complete ---")
