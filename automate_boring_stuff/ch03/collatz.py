def collatz(number):
    while number != 1:
        if number % 2 == 0:  # number is even number = number // 2
            number = number // 2
            print(f"{number}")
        else:  # number is odd
            number = 3 * number + 1
            print(f"{number}")


try:
    answer = int(input("Enter a number: "))
except ValueError:
    print("Integer number is required")
else:
    collatz(answer)
