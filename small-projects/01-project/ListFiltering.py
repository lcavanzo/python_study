"""
List Filtering: Write a function that filters a list of numbers, returning only the positive numbers.
Test it with an empty list, a list containing only negative numbers, and a list
containing mixed positive and negative numbers, including zero.
"""

from typing import List


def positiveNumbers(numbers: List[int]) -> List[int]:
    positive_list = []
    for number in numbers:
        if number >= 0:
            positive_list.append(number)
    return positive_list


lst1 = []
lst2 = [-1, -2, -5]
lst3 = [-1, 2, -3, 4, -5, 6, 0]


print(f"Positive numbers in {lst1} -> {positiveNumbers(lst1)}")
print(f"Positive numbers in {lst2} -> {positiveNumbers(lst2)}")
print(f"Positive numbers in {lst3} -> {positiveNumbers(lst3)}")

assert positiveNumbers(lst1) == [], "Test Case 1 Failed: Empty List"
assert positiveNumbers(lst2) == [], "Test Case 2 Failed: Negative Numbers"
assert positiveNumbers(lst3) == [2, 4, 6, 0], "Test Case 3 Failed: Mixed Numbers"

print("All test cases passed!")
