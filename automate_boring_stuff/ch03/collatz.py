"""
Write a function named collatz() that has one parameter named number. If number is even,
then collatz() should print number // 2 and return this value. If number is odd,
then collatz() should print and return 3 * number + 1
"""


def collatz(number):
    """Collatz function"""
    while number != 1:
        # check if number is even
        if number % 2 == 0:
            number = number // 2
        # check if number is odd
        else:
            number = 3 * number + 1
        print(f"{number}")
    return number


try:
    answer = int(input("Enter number: "))
    collatz(answer)
except ValueError:
    print("Oops! That was not a valid number. Try again...")
