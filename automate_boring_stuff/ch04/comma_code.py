# Comma code
"""
Write a function that takes a list value as an argument and returns a stringwith
with all the items separated by a comma and a space, with and inserted before the
last item. For example, passing the previous spam list to the function would
return 'apples, bananas, tofu, and cats'. But your function should be able
to work with any list value passed to it. Be sure to test the case where
an empty list [] is passed to your function.
"""


def phrase(words):
    """Receives a list and return all the words in the list as a simple phrase"""
    if len(words) == 0:
        print("please provide a list")
    elif len(words) == 1:
        print(words[0])
    else:
        for i in range(len(words)):
            if i == len(words) - 1:
                print(f"and {words[-1]}", end="")
                break
            print(words[i], end=" ")


spam = ["apples", "bananas", "tofu", "cats", "oranges", "dogs", "rhyno", "humans"]
spam = ["tests"]
phrase(spam)
