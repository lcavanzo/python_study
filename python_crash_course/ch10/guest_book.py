filename = 'guest_book.txt'

flag = True
while flag:
    guest_name = input("What is your name(q to quit): ")
    if guest_name == 'q':
        flag = False
    else:
        print(f"Hello {guest_name.title()}")
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name.title()}\n")
