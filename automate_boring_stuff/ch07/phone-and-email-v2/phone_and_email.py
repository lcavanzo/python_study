#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard

"""
Get the text off the clipboard.
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.
"""

import re

import pyperclip

phone_regex = re.compile(
    r"""(
        (\d{3}|\(\d{3}\))?              # area code, The ? matches zero or one of the preceding group.
        (\s|-|\.)?                      # separator
        (\d{3})                         # fist 3 digits
        (\s|-|\.)                      # separator
        (\d{4})                         # fist 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
        )
    """,
    re.VERBOSE,
)

# Create email regex
email_regex = re.compile(
    r"""(
        [a-zA-Z0-9._%+-]+   # username, The + matches one or more of the preceding group.
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name
        (\.[a-zA-Z]{2,4})   # dot-something
    )""",
    re.VERBOSE,
)

# Find matches in a clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[6] != "":
        phone_num += " x" + groups[6]
    if len(phone_num) > 9:
        matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("---------- Copied to clipboard ----------------")
    print("\n".join(matches))
else:
    print("No phone number or email addresses found ")
