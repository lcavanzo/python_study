# --- Handling FileNotFoundError ---

non_existent_file = "non_existent_data.txt"

try:
    with open(non_existent_file, "r") as file:
        content = file.read()
        print(f"Content: {content}")
except FileNotFoundError:
    print(
        f"Error: The file '{non_existent_file}' was not found. Please check the path."
    )
    # In an SRE context, you might log this error, alert an operator, or attempt to create a default file.
except PermissionError:
    print(f"Error: Permission denied to access '{non_existent_file}'.")
except IOError as e:
    print(f"An unexpected I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")

# Example of creating a file if it doesn't exist
config_template = "template_config.ini"
try:
    with open(config_template, "x") as file:
        file.write("[Database]\n")
        file.write("host=localhost\n")
        file.write("port=5432\n")
        file.write("[Application]\n")
        file.write("environment=development\n")
    print(f"Created new config template: {config_template}")
except FileExistsError:
    print(f"Config template '{config_template}' already exists. No new creation needed")
