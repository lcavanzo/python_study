# --- Demonstrating Different File Modes ---

# Mode 'x': Exclusive creation
new_config_file = "app_config.cfg"
try:
    with open(new_config_file, "x") as file:
        file.write("DEBUG=TRUE\n")
        file.write("LOG_LEVEL=INFO\n")
    print(f"Succesfully created a new config file: {new_config_file}")
except FileExistsError:
    print(f"Error: {new_config_file} already exists. Cannot create in 'x' mode.")
except IOError as e:
    print(f"An I/O error occured: {e}")

# Mode 'a': Appending to a file
log_file_path = "system_events.log"
with open(log_file_path, "a") as file:
    file.write("2025-10-27 10:05:00 - EVENT: System reboot scheduled.\n")
print(f"Appended to {log_file_path}")

with open(log_file_path, "a") as file:
    file.write("2025-10-27 10:10:00 - EVENT: Disk low warning.\n")
print(f"Appendend again to {log_file_path}")

# Reading the appended content
with open(log_file_path, "r") as file:
    print(f"\nContent of {log_file_path}:\n{file.read()}")

# Mode 'r+': Read and Write (Does not truncate)
# Let's create a temporary file first
temp_file = "temp_data.txt"
with open(temp_file, "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

print(f"\nInitial content of {temp_file}:")
with open(temp_file, "r") as f:
    print(f.read())

print(f"Using 'r+' mode on {temp_file}")
with open(temp_file, "r+") as f:
    initial_content = f.read()  # Reads all content
    print(f"Content after f.read() in r+ mode: \n{initial_content}")
    f.seek(0)  # Mode cursos back to beginning
    f.write("NEW ")  # Overwrites first part
    f.write("text\n")  # Continues overwriting, then writing new
    f.truncate()  # Truncates from current position to end(optional but good for porecise overwriting)

print(f"\nFinal content of {temp_file} after 'r+':")
with open(temp_file, "r") as f:
    print(f.read())
