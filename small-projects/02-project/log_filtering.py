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
- [ ] - Calculate SHA256 for error.log file
- [ ] - Save SHA256 value into error.log.sha256 file
"""

import re


def verify_and_process_log_file(filepath, file_errors):
    """
    Reads a log file.
    """
    # Step1: Read file
    print(f"--- Verifying log file: {filepath} ---")
    log = None
    try:
        with open(filepath) as f:
            log = f.readlines()
    except FileNotFoundError:
        print(f"Warning: file not found: {filepath}")
    except IOError as e:
        print(f"Error reading log file: {e}")

    # Step2: Create filteres errors file
    # print(log)
    if log:
        filter_errors(log, file_errors)
    else:
        print("No errors")

    # Validate errrors file -- funtions ?
    with open(file_errors, "r") as e_file:
        content = e_file.read()
    print(f"\n--- Verifying error log files: {file_errors} ---")
    print(content)

    # Step3: Calculate and save hash for errors file
    print(f"\n--- Verifying error log files: {file_errors} ---")


def filter_errors(logfile, file_errors):
    error_messages = []
    for linenum, line in enumerate(logfile, 1):
        columns = line.split()
        # reversed regex, find not 2xx matches
        if re.search(r"^(?!2\d\d)", columns[-2], re.IGNORECASE):
            error_messages.append(line)
    with open(file_errors, "w") as f:
        for error in error_messages:
            f.write(error)


# --- Demonstration ---
webserver_file = "webserver_access.log"
webserver_errors = "webserver_errors.log"

## Create sample file
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
        '192.168.1.200 - - [27/Oct/2023:10:00:20 +0000] "GET /nonexistent HTTP/1.1" 299 100\n'
    )

verify_and_process_log_file(webserver_file, webserver_errors)
