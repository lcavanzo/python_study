def read_log_file(filepath):
    """
    Reads a log file line by line and yields each line.
    Args:
        filepath (str): The path to the log file
    Yields:
        str: Each line from the logs file
    """
    try:
        with open(filepath, "r") as f:
            for line in f:
                yield line.strip()  # .strip() removes leading/trailing whitespaces, including  newline
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        # In a real application, you might raise a custom exception or log for this.
        return  # Strop execution if file not found
    except PermissionError:
        print(f"Error: Permission denied to access '{filepath}'.")
        return
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        return


# Example of usage:
if __name__ == "__main__":
    log_file_path = "sample.log"
    # Create a dummy log file for demonstration
    with open(log_file_path, "w") as f:
        f.write(
            "[2026-10-26 10:30:45] INFO: User 'admin' accessed /dashboard from 192.168.1.10.\n"
        )
        f.write(
            "[2026-10-26 10:31:02] WARNING: Disk space low on /var/log. Current usage: 90%.\n"
        )
        f.write(
            "[2026-10-26 10:31:15] ERROR: Failed to connect to database at db.example.com. Connection refused.\n"
        )
        # Malformed line for error handling test
        f.write("This is an malformed line.\n")
        f.write("[2023-10-26 10:32:01] INFO: Application started successfully.\n")

    print(f"Reading log file: {log_file_path}")
    for log_entry in read_log_file(log_file_path):
        print(log_entry)
