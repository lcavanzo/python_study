"""
You are given a list called my_list. Using this list, you must create a tuple called my_tuple.
The tuple will contain the list’s first element, last element, and the length of the list,
in that same order.

Sample Input#
my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
Sample Output
my_tuple = (34, "Hannibal", 5)

"""

my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]

# Write your code her
my_tuple = (my_list[0], my_list[-1], len(my_list))
print(my_tuple)
