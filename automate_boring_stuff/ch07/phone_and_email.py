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
# TODO: Find matches in a clipboard text.
# TODO: Copy results to the clipboard
