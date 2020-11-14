filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    # stores the file in a list
    lines = file_object.readlines()

for line in lines:
    print(f"{line.rstrip()}")

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)

