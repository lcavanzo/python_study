
def collatz(number):
    """defining the collatz sequence demostration"""
    while number != 1:
        if number % 2 == 0: # if number is even
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
    return number

try:
    number = int(input("Write a number: "))
    collatz(number)
except ValueError:
    print("Must be an integer number")
