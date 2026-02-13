"""
Task: Simulate a binary data transfer.
- [x] - Create a small binary file (e.g., write random bytes to it, or just a known string in binary mode) and calculate its MD5 hash.

- [x] - Then, simulate a corrupted transfer by modifying a few bytes in the file directly (e.g., using seek() and write() in 'r+b' mode).

- [x] - Finally, attempt to verify the integrity using the original MD5 hash.

"""

import os
import hashlib
import random  # For potentially more random "corruption"

# --- Constants
BINARY_FILENAME = "binary_data.bin"
INITIAL_CONTENT_SIZE = 1024  # ~1KB of data


def create_binary_file(filepath, content_size=INITIAL_CONTENT_SIZE):
    """
    Creates a binary file with initial content.
    """
    print(f"Creating binary file: {filepath}")
    with open(filepath, "wb") as f:
        # Write some initial binary content (e.g., random bytes or a repeating string)
        # Using a repeating string makes it easier to test specific byte modifications
        initial_data = b"This is some initial binary content for testing integrity. "
        # Ensure total size is roughly content_size
        f.write(initial_data * (content_size // len(initial_data) + 1))
        # Trim to exact size if desired
        f.seek(0)
        f.truncate(content_size)


def calculate_hash(filepath, algorithm="md5", block_size=65536):
    """
    Calculate hash for a file.
    Args:
        filepath: path of the file
        algorithm: 'md5' by default, can also be 'sha256', etc.
        block_size: size of each shard for hashing, 65536 by default.
    Returns:
        hash: hex digest of the file's hash, or None if an error occurs.
    """
    try:
        hasher = hashlib.new(algorithm)  # More flexible way to get a hasher
    except ValueError:
        print(f"Error: Unsupported hashing algorithm '{algorithm}'")
        return None

    try:
        with open(filepath, "rb") as f:
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while hashing {filepath}: {e}")
        return None
    return hasher.hexdigest()


def simulate_corruption(filepath, offset=50, num_bytes_to_corrupt=5):
    """
    Simulates a corrupted transfer by modifying a few bytes in the file.
    Uses seek() and write() in 'r+b' mode.
    """
    print(
        f"Simulating corruption in '{filepath}' by modifying {num_bytes_to_corrupt} bytes at offset {offset}..."
    )
    try:
        with open(filepath, "r+b") as f:  # Open in read/write binary mode
            f.seek(offset)  # Move to the desired offset
            # Generate random bytes for corruption
            corrupted_bytes = os.urandom(num_bytes_to_corrupt)
            f.write(corrupted_bytes)  # Overwrite existing bytes
        print("Corruption simulated successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}. Cannot corrupt.")
    except IOError as e:
        print(f"Error corrupting file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during corruption: {e}")


## --- Demonstration ---

# 1. Ensure a clean slate for the demonstration
if os.path.exists(BINARY_FILENAME):
    os.remove(BINARY_FILENAME)
    print(f"Removed existing file: {BINARY_FILENAME}")

# 2. Create the initial binary file and calculate its MD5 hash
create_binary_file(BINARY_FILENAME)
print(f"\n--- Calculating initial MD5 for '{BINARY_FILENAME}' ---")
original_md5_hash = calculate_hash(BINARY_FILENAME)

if original_md5_hash:
    print(f"Original MD5 hash: {original_md5_hash}")
else:
    print("Failed to calculate original MD5 hash. Exiting.")
    exit()

# 3. Simulate a corrupted transfer by modifying a few bytes
print(f"\n--- Simulating unauthorized modification in '{BINARY_FILENAME}' ---")
simulate_corruption(
    BINARY_FILENAME, offset=random.randint(0, INITIAL_CONTENT_SIZE - 10)
)  # Corrupt at a random spot

# 4. Calculate the MD5 hash of the (now potentially corrupted) file
print(f"\n--- Calculating MD5 for the (potentially corrupted) '{BINARY_FILENAME}' ---")
corrupted_md5_hash = calculate_hash(BINARY_FILENAME)

if corrupted_md5_hash:
    print(f"MD5 hash after 'transfer': {corrupted_md5_hash}")
else:
    print("Failed to calculate MD5 hash after simulated corruption. Exiting.")
    exit()

# 5. Verify integrity using the original MD5 hash
print("\n--- Verifying Integrity ---")
if original_md5_hash == corrupted_md5_hash:
    print(f"Integrity check PASSED for {BINARY_FILENAME}.")
else:
    print(f"Integrity check FAILED for {BINARY_FILENAME}. Data has been altered!")
    print(f"Original hash: {original_md5_hash}")
    print(f"Corrupted hash: {corrupted_md5_hash}")

# 6. Optional: Clean up the created file
os.remove(BINARY_FILENAME)
# print(f"\nCleaned up: {BINARY_FILENAME}")
