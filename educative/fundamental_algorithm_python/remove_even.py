"""
Given a list of integers, lst, remove all the even integers from the list.
"""


def remove_even(lst):
    # Replace this placeholder return statement with your code
    nlst = []
    for item in lst:
        # print(f"item {item}")
        if item % 2 != 0:
            nlst.append(item)
    # print(f"new list {nlst}")
    return nlst


lst = [0, 20, 41]
# lst = [2, 4, 6, 8, 10, 13, 15]
print(remove_even(lst))
