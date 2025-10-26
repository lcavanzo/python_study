"""
Write a function called calculate_average that takes a list of numbers as input and returns the average of the numbers.
Include a check to handle the case where the list is empty (return 0 in that case).
"""


def calculate_average(numbers):
    total = 0
    if len(numbers) == 0:
        return 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg


numP = [1, 2, 3, 4, 5]
numPZ = [0, 1, 2, 3, 4, 5]
numN = [-1, -2, -3, -4, -5]
numZ = []


# print(calculate_average(numP))
# print(calculate_average(numPZ))
# print(calculate_average(numN))
# print(calculate_average(numZ))
