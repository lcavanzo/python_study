"""
Write a Python function parse_semantic_version(version_string) that takes a string and validates if it adheres to a simplified semantic versioning format: MAJOR.MINOR.PATCH. MAJOR, MINOR, and PATCH must be non-negative integers.

The function should return a dictionary with keys 'major', 'minor', 'patch' if valid, otherwise None.

Example Valid Inputs:

    "1.0.0"
    "0.5.20"
    "123.456.789"

Example Invalid Inputs:

    "1.0" (missing patch)
    "1.0.0-beta" (extra characters)
    "1.A.0" (non-digit in minor)
    ".1.0" (leading dot)

"""

import re


def parse_semantic_version(version_string):
    """
    Validates if a string adheres to MAJOR.MINOR.PATCH format and
    returns a dictionary with 'major', 'minor', 'patch' as integers if valid,
    otherwise None.
    """
    # Regex: ^ (start of string)
    # (?P<major>\d+) (named group 'major', one or more digits)
    # \. (literal dot)
    # (?P<minor>\d+) (named group 'minor', one or more digits)
    # \. (literal dot)
    # (?P<patch>\d+) (named group 'patch', one or more digits)
    # $ (end of string)
    pattern = re.compile(r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$")
    match = pattern.search(version_string)

    if match:
        return {
            "major": int(match.group("major")),
            "minor": int(match.group("minor")),
            "patch": int(match.group("patch")),
        }
    else:
        return None


inputs = [
    "1.0.0",
    "0.5.20",
    "123.456.789",
    "1.2-beta.3",
    "1.0",
    "1.0.0-beta",
    "1.A.0",
    ".1.0",
]

if __name__ == "__main__":
    for item in inputs:
        result = parse_semantic_version(item)
        print(f"'{item}' -> {result}")
