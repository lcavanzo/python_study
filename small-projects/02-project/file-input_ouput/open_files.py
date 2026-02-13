# --- Opening and Closing Files Safely with 'with' Statement ---

# Example 1: Writing to a new text file

file_path_write = "my_log.txt"
try:
    with open(file_path_write, "w") as file:  # 'w' mode for Writing
        file.write("Application started succesfully.\n")
        file.write("User 'admin' logged at 2025-10-27 10:00:00.\n")
    print(f"Content succesfully written to {file_path_write}")

    # Example 2: reading from the same file
    with open(file_path_write, "r") as file:  # 'r' mode for reading
        content = file.read()
        print(f"\nContent of {file_path_write}:\n{content}")

except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
