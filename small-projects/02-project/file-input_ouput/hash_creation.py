import hashlib


def calculate_file_hash(
    filepath: str, algorithm: str = "sha256", block_size: int = 65536
):
    """
    Calculates the hash of a file using the specified algorithm.

    Args:
        filepath (str): The path to the file.
        algorithm (srr): The hasing algorithm to use (md5 or sha256).
        block_size (int) The size of chunks to read from the file (in bytes).

    Returns:
        str: The hexadecimal hash digest of the file, or None if file not found.
    """

    try:
        # Get the appropiate hash object based on the algorithm
        if algorithm == "md5":
            hasher = hashlib.md5()
        elif algorithm == "sha256":
            hasher = hashlib.sha256()
        else:
            raise ValueError("Unsupported hasing algorithm. Choose 'md5' or 'sha256'")

        # Open the file in binary read mode('rb')
        with open(filepath, "rb") as f:
            while True:
                # Read the file in chunks
                buffer = f.read(block_size)
                if not buffer:
                    break  # End of file
                hasher.update(buffer)  # Update the hasher with the current chunk
        return hasher.hexdigest()  # Return the hexadecimal representation of the digest

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An unexpected errro occurred: {e}")
        return None


# Example of Usage

# Create a sample file for integrity testing
test_file_path = "critical_script.py"
with open(test_file_path, "w") as f:
    f.write("import os\n")
    f.write("def do_something_important():\n")
    f.write("    print('Performing critical operation...')\n")
    f.write("    # Simulate a critical operation\n")
    f.write("    with open('operation_log.txt', 'a') as log_f:\n")
    f.write("        log_f.write('Critical operation performed.\\n')\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    do_something_important()\n")

print(f"Created sample file: {test_file_path}")

# Calculate hashes
md5_hash = calculate_file_hash(test_file_path, algorithm="md5")
sha256_hash = calculate_file_hash(test_file_path, algorithm="sha256")

print(f"MD5 Hash of '{test_file_path}': {md5_hash}")
print(f"SHA256 Hash of '{test_file_path}': {sha256_hash}")

# Now, let's modify the file slightly
with open(test_file_path, "a") as f:
    f.write("\n# Added a comment later")

print(f"\nModified file: {test_file_path}")

# Recalculate hashes after modification
md5_hash_modified = calculate_file_hash(test_file_path, algorithm="md5")
sha256_hash_modified = calculate_file_hash(test_file_path, algorithm="sha256")

print(f"MD5 Hash (modified) of '{test_file_path}': {md5_hash_modified}")
print(f"SHA256 Hash (modified) of '{test_file_path}': {sha256_hash_modified}")

