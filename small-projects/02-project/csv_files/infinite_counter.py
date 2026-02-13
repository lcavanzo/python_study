def infinite_counter():
    num = 1
    while True:  # infinite loop
        yield num
        num += 1  # Python remembers this state for next time


# 1. Initialize the machine (The code DOES NOT run yet)
gen = infinite_counter()

# 2. Pull the lever once
print(next(gen))  # Output: 1

# 3. Pull the lever again
print(next(gen))  # Output: 2

# 4. Pull the lever again
print(next(gen))  # Output: 3
