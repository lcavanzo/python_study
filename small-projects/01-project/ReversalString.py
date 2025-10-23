"""
String Reversal: Write a function that reverses a string. Test it with
an empty string, a single-character string, and a palindrome string.
"""


def reversalStr(words: str) -> str:
    return words[::-1]


string1 = ""
string2 = "A"
string3 = "Anita lava la tina"
string4 = "racecar"  # added a perfect palindrome


print(f"'{string1}' -> '{reversalStr(string1)}'")
print(f"'{string2}' -> '{reversalStr(string2)}'")
print(f"'{string3}' -> '{reversalStr(string3)}'")
print(f"'{string4}' -> '{reversalStr(string4)}'")

assert reversalStr(string1) == ""
assert reversalStr(string2) == "A"
assert reversalStr(string3) == "anit al aval atinA"
assert reversalStr(string4) == "racecar"

print("All test cases passed!")
