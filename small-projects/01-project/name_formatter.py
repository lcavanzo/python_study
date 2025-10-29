# name_formatter.py
import string

# string.punctuantion include the following:
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


def format_name(first, last):
    if first == "":
        return last
    if last == "":
        return first
    if first == "" and last == "":
        return ""
    if first is None or last is None:
        raise ValueError("Invalid Name")
    return first.strip("!,. -") + " " + last.strip("-!,. ")
