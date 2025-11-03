import hashlib


def calculate_file_hash(filepath, algorithm="sha256", block_size=65536):
    """
    (Same function as above for clarity in this section)
    Calculates the hash of a file using the specified algorithm.
    """
    try:
        if algorithm == "md5":
            hasher = hashlib.md5()
        elif algorithm == "sha256":
            hasher = hashlib.sha256()
        else:
            raise ValueError("Unsupported hashing algorithm. Choose 'md5' or 'sha256'.")

        with open(filepath, "rb") as f:
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except IOError:
        return None
    except ValueError:
        return None
    except Exception:
        return None


def verify_file_integrity(filepath, expected_hash, algorithm="sha256"):
    """
    Verifies the integrity of a file by comparing its calculated hash
    against an expected hash.

    Args:
        filepath (str): The path to the file.
        expected_hash (str): The known, good hash value for comparison.
        algorithm (str): The hashing algorithm to use ('md5' or 'sha256').

    Returns:
        bool: True if the file's hash matches the expected_hash, False otherwise.
    """
    current_hash = calculate_file_hash(filepath, algorithm)
    if current_hash is None:
        print(f"Could not calculate hash for {filepath}. Integrity check failed.")
        return False

    if current_hash == expected_hash:
        print(f"Integrity check PASSED for '{filepath}' using {algorithm.upper()}!")
        return True
    else:
        print(f"Integrity check FAILED for '{filepath}' using {algorithm.upper()}!")
        print(f"  Expected: {expected_hash}")
        print(f"  Current:  {current_hash}")
        return False


# --- Example of Verifying File Integrity ---

critical_config = "prod_config.ini"
# Initial state of the critical config file
with open(critical_config, "w") as f:
    f.write("[Server]\n")
    f.write("port = 8080\n")
    f.write("hostname = production.example.com\n")
    f.write("[Database]\n")
    f.write("db_user = prod_user\n")
    f.write("db_pass = secure_password123\n")

print(f"Created initial critical config: {critical_config}")

# 1. Calculate and store a trusted hash (e.g., in a secure database, version control, or separate file)
trusted_sha256_hash = calculate_file_hash(critical_config, "sha256")
print(f"Trusted SHA256 hash recorded: {trusted_sha256_hash}")

print("\n--- Performing initial integrity check ---")
verify_file_integrity(critical_config, trusted_sha256_hash, "sha256")

# 2. Simulate an unauthorized modification
print(f"\n--- Simulating unauthorized modification to {critical_config} ---")
with open(critical_config, "w") as f:  # Overwriting the file (truncates)
    f.write("[Server]\n")
    f.write("port = 8081\n")  # Port changed!
    f.write("hostname = production.example.com\n")
    f.write("[Database]\n")
    f.write("db_user = prod_user\n")
    f.write("db_pass = secure_password123\n")  # Content altered
print("File content has been subtly changed.")

# 3. Perform integrity check after modification
print("\n--- Performing integrity check after modification ---")
verify_file_integrity(critical_config, trusted_sha256_hash, "sha256")

# 4. Simulate restoration to original state
print(f"\n--- Simulating restoration of {critical_config} to original state ---")
with open(critical_config, "w") as f:
    f.write("[Server]\n")
    f.write("port = 8080\n")
    f.write("hostname = production.example.com\n")
    f.write("[Database]\n")
    f.write("db_user = prod_user\n")
    f.write("db_pass = secure_password123\n")
print("File content restored.")

# 5. Perform integrity check after restoration
print("\n--- Performing integrity check after restoration ---")
verify_file_integrity(critical_config, trusted_sha256_hash, "sha256")
