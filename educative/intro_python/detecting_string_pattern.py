"""
Detecting String Pattern
In this coding exercise, you are asked to write the body of a function called detect_pattern that returns true or false
depending upon whether two strings have the same pattern of characters. More precisely, two strings have the same pattern
if they are of the same length and
if two characters in the first string are equal
if and only if the characters in the corresponding positions in the second string are also equal.

Below are some examples of patterns that are the same and patterns that differ:

1st String	2nd String	Same Pattern
“”	“”	True
“a”	“a”	True
“x”	“y”	True
“ab”	“xy”	True
“aba”	“xyz”	False
“- - -”	“xyz”	False
“- - -”	“aaa”	True
“xyzxyz”	“toetoe”	True
“xyzxyz”	“toetoa”	False
“aaabbbcccd”	“eeefffgggz”	True
“cbacbacba”	“xyzxyzxyz”	True
“abcdefghijk”	“lmnopqrstuv”	True
“asasasasas”	“xxxxxyyyyy”	False
“ascneencsa”	“aeiouaeiou”	False
“aaasssiiii”	“gggdddfffh”	False
For example, if two strings called s1 and s2 contain the following letters:

s1 = "aba"
s2 = "xyz"
then the call detect_pattern(s1, s2) should return False.

Note:

The function detect_pattern takes two parameters: the two strings to compare.
You are allowed to create new strings, but otherwise you are not allowed to construct extra data structures to solve this problem (no list, set, dictionary, etc).
Keep in mind that the method should return the same value no matter what order the two strings are passed.
"""

# You are allowed to create new strings,
# but otherwise you are not allowed to construct
# extra data structures to solve this problem (no list, set, dictionary, etc).


def detect_pattern(s1, s2):  # this function takes two parameters as strings to compare.
    # Keep in mind that this method should return the same value
    # no matter what order the two strings are passed

    # Insert your code here
    if len(s1) == len(s2):
        if s1 == s1[::-1] and s2 == s2[::-1]:
            return True
    return False


s1 = "aba"
s2 = "xyz"

a1 = "asasasasas"
a2 = "xxxxxyyyyy"

b1 = "abcdefghijk"
b2 = "lmnopqrstuv"
print(detect_pattern(s1, s2))
print(detect_pattern(a1, a2))
print(detect_pattern(b1, b2))
