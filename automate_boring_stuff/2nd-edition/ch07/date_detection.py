#! python3
# date_detection.py - Detect if a date is valid

"""
* RE detect dates in the format DD/MM/YYYY
* Store that date in day,month,year variales
* Detect if a date is valid:
     April(4), June(6), September(9), and November(11) have 30 days, February(2) has 28 days
     and the rest of the months have 31 days.
     February has 29 days in leap years.
     Leap years are every year evenly divisible by 4,
     except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
"""

import re

import pyperclip


# check if a year is a leap year
def is_leap_year(leap_year):
    """
    Getting leap year
    """
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        return True
    else:
        return False


# capturing the date DD/MM/YYYY
date_regex = re.compile(
    r"""(
        (0[1-9]|[12][0-9]|3[01])    # day -> 0-9 or 10-29 or 30 - 31
        \/                          # separator
        (0[1-9]|1[0-2])             # month -> 01-09,10-12
        \/                          # separator
        ([12]\d{3})                 # year -> 1000 - 2999
    )""",
    re.VERBOSE,
)

# Find matches in the clipboard
dates = str(pyperclip.paste())

matches = []
for groups in date_regex.findall(dates):
    date = "/".join([groups[1], groups[2], groups[3]])
    matches.append(date)

for match in matches:
    day, month, year = match.split("/")

    # April(4), June(6), September(9), and November(11) have 30 days
    if (month == "04") | (month == "06") | (month == "09") | (month == "11"):
        if int(day) <= 30:
            print(f"{day}/{month}/{year} is a valid date")

    # January(1), March(3), May(5), July(7), August(8), October(10) and December(12) have 31 days
    if (
        (month == "01")
        | (month == "03")
        | (month == "05")
        | (month == "07")
        | (month == "08")
        | (month == "10")
        | (month == "12")
    ):
        if int(day) <= 31:
            print(f"{day}/{month}/{year} is a valid date")

    # February(2) has 28 days, 29 in leap years
    if month == "02":
        year = int(year)
        if int(day) <= 28:
            print(f"{day}/{month}/{year} is a valid date")
        # Show a leap year
        if is_leap_year(year):
            if int(day) <= 29:
                print(f"{day}/{month}/{year} is a valid date - whoa leap year")
