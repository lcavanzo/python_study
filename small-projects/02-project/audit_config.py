"""
Task: Write a function audit_config_file(filepath, baseline_hash_file) that takes a configuration file path and a path to a file containing its baseline SHA256 hash. The function should:

- [x] - Read the baseline hash. If the baseline_hash_file does not exist, it should calculate the current hash of filepath, save it to baseline_hash_file, and report that a new baseline was established.

- [ ] - If the baseline_hash_file exists, compare the current hash of filepath with the baseline.

- [ ] - Print a clear message indicating whether the configuration file's integrity passed or failed the audit.

- [ ] - Handle FileNotFoundError for both the config file and the hash file gracefully.

Hint: Adapt the calculate_file_hash and verify_file_integrity functions from the lesson.


"""

import hashlib
import json


def verify_file_integrity(filepath, baseline_hash_file):
    hash_filepath = calculate_hash(filepath)
    hash_baseline_content = read_file(baseline_hash_file)
    print(hash_filepath)
    print(hash_baseline_content)

    if hash_baseline_content == hash_filepath:
        print(f"--- File Integrity passed: {filepath} == {baseline_hash_file}---")
    elif hash_baseline_content is None:
        print("--- New baseline hash file was established ---")
        new_baseline_hash = calculate_hash(filepath)
        with open(baseline_hash_file, "w") as f:
            f.write(new_baseline_hash)
        print(new_baseline_hash)
        print(f"Filename: {baseline_hash_file}")
    elif hash_baseline_content != hash_filepath:
        print("--- File Integrity Not Passed, please verify it ---")


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
        raise ValueError("Unsupported hashing algorithm. Choose 'md5' or 'sha256'.")
    try:
        with open(filepath, "rb") as f:
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
    except FileNotFoundError:
        print(f"Error: File Not Found {filepath}")
    except IOError as e:
        print(f"Error reading file {e} ")
    except Exception as e:
        print(f"An unexpected error occureed: {e}")
    return hasher.hexdigest()


def read_file(filepath, mode="r"):
    """
    Read a file in read mode only by default
    Args:
        filepath: path of the file
        mode(optional): open mode, read by default
    return:
        content: content of the file

    """

    content = None
    try:
        with open(filepath, mode) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File Not Found {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {e} ")
        return None
    except Exception as e:
        print(f"An unexpected error occureed: {e}")
        return None
    return content


# - Demonstation
audit_file = "audit-config.json"
audit_file_hash = f"{audit_file}.sha256"


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

# with open(audit_file, "w") as f:
#     json.dump(audit_config_data, f)
#
verify_file_integrity(audit_file, audit_file_hash)
