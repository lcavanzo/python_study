# name_formatter.py
def format_name(first, last):
    if first == "":
        return last
    if last == "":
        return first
    if first is None or last is None:
        # This is currently inconsistent, let's fix it with TDD
        return "Invalid Name"
    return first + " " + last
