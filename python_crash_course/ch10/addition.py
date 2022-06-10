while True:
    try:
        num1 = input("First number to add: ")
        if num1 == 'q':
            break
        num1 = int(num1)
        num2 = input("Second number to add: ")
        if num2 == 'q':
            break
        num2 = int(num2)
    except ValueError:
        print("Values must be numbers!!!")
    else:
        print(int(num1) + int(num2) )
