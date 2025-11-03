"""
Arguments and Return Values: Write a function called greet_person that takes two arguments: name (a string) and greeting (a string with a default value of "Hello").
The function should return a greeting string like "Hello, Alice!".

Write tests to check both the case where the default greeting is used and where a custom greeting is provided
"""


def greet_person(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name.capitalize()}"


# print(greet_person("luis"))
# print(greet_person("cavanzo", "sir"))
