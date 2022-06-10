def print_content(filename):
    """Print the content of a file"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    else:
        print(f"filename: {filename}:\n{content.strip()}")


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_content(filename)
