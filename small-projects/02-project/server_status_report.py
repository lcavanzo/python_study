"""
Task: Write a Python script that simulates monitoring a server's status.
It should:
    Read server names from a file named servers.txt (one server name per line).

    For each server, simulate checking its status (e.g., print "Checking status for <server_name>..."). You don't need to actually ping a server.

    Generate a server_status_report.txt file. For each server, write its name and a simulated status (e.g., "UP", "DOWN", "DEGRADED").

    After generating the report, calculate its SHA256 hash and write this hash to a separate file named server_status_report.sha256.

    The next time the script runs, it should first verify the integrity of the existing server_status_report.txt against its stored hash. If the integrity check fails, it should print a warning before generating a new report.

"""

import os
import random
import hashlib


def validate_integrity(filename, filename_checksum):
    """
    Generate server report if not existing
    """
    server_report = "server_status_report.txt"

    # try to read report
    report_content = load_file(filename)

    # Comparing current hashing with the hashing in the checksum file
    if os.path.exists(filename_checksum):
        print("Comparing hashing")
        compare_hashing(filename_checksum, calculate_file_hash(server_report))

    else:
        if os.path.exists(server_report):
            print(f"Creating {filename_checksum}")
            current_hash = calculate_file_hash(server_report)
            if current_hash is None:
                return
            try:
                with open(filename_checksum, "w") as f:
                    f.write(current_hash)
            except FileNotFoundError as e:
                print(f"Error: {e}")
            except IOError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

        else:
            try:
                with open(server_report, "x") as f:
                    if report_content is None:
                        return
                    for line in report_content.splitlines():
                        server_name = line.split()
                        status = random.choice(["UP", "DOWN", "DEGRADED"])
                        match status:
                            case "UP":
                                print(f"Cheking status -> {server_name[0]} {status}")
                                f.write(f"{server_name[0]} -> {status}\n")
                            case "DOWN":
                                print(f"Cheking status -> {server_name[0]} {status}")
                                f.write(f"{server_name[0]} -> {status}\n")
                            case "DEGRADED":
                                print(f"Cheking status -> {server_name[0]} {status}")
                                f.write(f"{server_name[0]} -> {status}\n")
                print(f"\n{server_report} generated successfuly")
            except FileExistsError:
                print(f"{server_report} exists.")
            except FileNotFoundError as e:
                print(f"Error: {e}")
                return
            except IOError as e:
                print(f"Error: {e}")
                return
            except Exception as e:
                print(f"Error: {e}")
                return


def compare_hashing(filename_hash, current_hash):
    """
    compare current hash with the previous hashing
    """
    file_hash = load_file(filename_hash)
    if file_hash == current_hash:
        print("same hash")
    else:
        print("different hash")


def calculate_file_hash(server_status_report, algorithm="sha256", block_size=65536):
    """
    Calculates the hash of a file using the specified algorithm.
    Reads the file in chunks for memory efficiency.
    Returns the hexadecimal hash string, or None if an error occurs.
    """
    if algorithm == "sha256":
        hasher = hashlib.sha256()
    elif algorithm == "md5":
        hasher = hashlib.md5()
    else:
        print(
            f"Error: Unsupported hashing algorithm '{algorithm}'. Choose 'md5' or 'sha256'."
        )
        return None
    try:
        with open(server_status_report, "rb") as f:
            while True:
                buffer = f.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
            return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found for hashing: {server_status_report}")
        return None
    except IOError as e:
        print(f"Error reading file {server_status_report} for hashing: {e}")
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred during hash calculation for {server_status_report}: {e}"
        )
    return None


def load_file(filename):
    """
    Load the filename content
    args:
        efilename: file to Load
    return:
        content -> list: content of the filename
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except IOError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


## Demonstration
# Creating server.txt file
server_filename = "servers.txt"
server_report_checksum = "server_status_report_sha256"


def _create_server_file():
    """
    Create server tmp file
    """
    try:
        with open(server_filename, "x") as f:
            f.write("server01 192.168.100.1\n")
            f.write("server02 192.168.100.2\n")
            f.write("server03 192.168.100.3\n")
            f.write("server04 192.168.100.4\n")
            f.write("server05 192.168.100.5\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def _clean_files(server_file, server_report):
    """
    Clean files like server_filename and server_status_report
    """
    if os.path.exists(server_filename):
        os.remove(server_filename)


# _create_server_file()

validate_integrity(server_filename, server_report_checksum)
