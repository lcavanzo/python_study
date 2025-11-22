"""
Task: Create a command-line Python script that manages a simple to-do list.
The list should be stored in a plain text file, where each line represents a to-do item.

Your script should support the following functionalities:
    add <item>: Adds a new item to the list.
    list: Displays all items in the list.
    remove <item_number>: Removes an item by its line number.
    clear: Deletes all items from the list.

Constraints: All data must be persisted in a single text file (e.g., todos.txt). You'll need to read the file, modify its content in memory, and then write the entire updated content back to the file.
"""


def add_item(filepath, item):
    """
    Add Item to the todo list
    """

    try:
        with open(filepath, "a") as f:
            f.write(item)
            f.write("\n")
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def list_items(filepath):
    """
    List all items in the todo list
    """
    try:
        with open(filepath, "r") as f:
            content = f.readlines()

    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    if content:
        for row, line in enumerate(content, 1):
            print(f"{row}) {line.strip()}")
    else:
        print("Todo list is empty")
        return
    return True


def remove_item(filepath, row):
    """
    Remove item from the todo list
    """
    try:
        with open(filepath, "r+") as f:
            lines = f.readlines()
            try:
                row = int(row)
            except ValueError:
                print("Error: Invalid Value")
                return
            if row > len(lines) or row < 1:
                print("Invalid number")
                return
            else:
                removed_item = lines.pop(row - 1)
                # del lines[row - 1]
                f.seek(0)
                f.writelines(lines)
                f.truncate()
                print(f"Item completed: {removed_item}")
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def clean_list(filepath):
    """
    Clear all the todo list
    """

    try:
        with open(filepath, "w") as f:
            f.write("")
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def menu(filepath):
    """
    Show menu
    """

    option = input("\nPlease select and option(add,list,remove,clear,exit)\n>> ")
    option = option.strip().lower()
    match option:
        case "add":
            item = input("Type what do you want to add>> ")
            add_item(filepath, item.lower().strip())
        case "list":
            list_items(filepath)
        case "remove":
            if list_items(filepath):
                row = input("Select row number to delete>> ")
                remove_item(filepath, row)
        case "clear":
            print("Cleaning TO-DO file")
            clean_list(filepath)
        case "exit":
            print("Thanks, have a nice day")
            exit()
        case _:
            print("Error: Invalid option\n")
            return


def main(filepath):
    """
    Principal function to keep the to-do list running
    """
    while True:
        menu(filepath)


# Demonstration
if __name__ == "__main__":
    filename = "todo_list.txt"
    main(filename)
