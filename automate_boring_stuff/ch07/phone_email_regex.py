#! python3
#  Finds phone numbers and email addresses on the clipboard.

"""
# what to do
-----------------------------------------------------------------------------
1. Get text from clipboard
2. Create 2 regex(phone number and email)
3. Return text to clipboard


# Roadmap
-----------------------------------------------------------------------------
1. Use pyperlip module to copy and paste string
2. Create 2 regexes, one for matching numbers and other for matching emails
3. Find all matches, not just the first, of both regexes
4. Neatly format the matches strings into a single string to paste.
5. Display some kind of message if no matches were found in the text

"""

import re

import pyperclip

phoneRegex = re.compile(
    r"""(
    (?:\+1\s?)?          # Optional country code with optional space (e.g., +1 or +1 )
    \(?([2-9][0-9]{2})\)? # Area code (2xx-9xx) with optional parentheses
    [\s.-]?               # Separator (space, hyphen, or dot)
    ([2-9][0-9]{2})       # First three digits of the local number
    [\s.-]?               # Separator
    ([0-9]{4})            # Last four digits of the local number
    )""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )""",
    re.VERBOSE,
)

phones_matches = re.findall(phoneRegex, pyperclip.paste())
emails_matches = re.findall(emailRegex, pyperclip.paste())

phones = []
for p in phones_matches:
    phones.append(p[0])

emails = []
for e in emails_matches:
    emails.append(e[0])

matches = phones + emails

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to the clipboard")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found")


"""
text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[6] != "":
        phoneNum += " x" + groups[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to the clipboard")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found")

"""
