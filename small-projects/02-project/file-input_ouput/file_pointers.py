# --- Demostrating File Pointers with seek() and tell() ---

pointer_demo_file = "pointer_test.txt"
with open(
    pointer_demo_file, "w+"
) as f:  # w+ mode for read/write, creates if not exists
    f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(f"Initial content written to {pointer_demo_file}")

    print(f"\nCurrent position (after writing): {f.tell()}")  # should be 26

    f.seek(0)  # Move to the beginning of the file
    print(f"Position after seek(0): {f.tell()}")  # should be 0

    firt_five = f.read(5)  # Read first 5 characters
    print(f"Read first 5 characters: '{firt_five}'")
    print(f"Position after reading 5 chars: {f.tell()}")  # should be 5

    f.seek(10, 0)  # Move to 10th byte from the beginning
    print(f"Position after seek(10,0): {f.tell()}")  # should be 10
    next_three = f.read(3)
    print(f"Read next 3 characters: '{next_three}'")
    print(f"Position after reading 3 chars: {f.tell()}")  # should be 13

    # Using seek to overwrite a specific part of the file
    f.seek(7, 0)  # Go to the 8th character(index 7)
    f.write("123")  # overwrite 'HIJ' with '123'
    print(f"Position after writing '123': {f.tell()}")

    # Read the whoe file to see the changes
    f.seek(0)
    final_content = f.read()
    print(f"Final content after seeking and writing: {final_content}")
    # Expected: ABCDEFG123KLMNOPQRSTUVWXYZ
