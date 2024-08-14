# table_printer.
"""
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
"""

table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

"""
OUTPUT
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""


def print_table(data):
    """
    Return right formatted table
    """
    # Create a list with the size of inner list
    col_widths = [0] * len(data)

    # Get the longest string count in each inner list
    for index, _ in enumerate(data):
        for value in data[index]:
            if len(value) > col_widths[index]:
                col_widths[index] = len(value)
        # Get total of rows for the table

    # print right formatted table
    for row in range(len(data[0])):
        print()
        for column in range(len(data)):
            print(f"{data[column][row]}".rjust(col_widths[column]), end=" ")


print_table(table_data)
