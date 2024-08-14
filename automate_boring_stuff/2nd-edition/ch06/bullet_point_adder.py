#! python3
"""
bullet_point_adder.py - Adds Wikipedia bulet pionts to the start of each
line of text on the clipboard

e.g.
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""
import pyperclip

text = pyperclip.paste()

# separate lines and add starts.
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indezes in the "lines" list
    lines[i] = f"* {lines[i]}"  # Add star to each string in "lines" list
text = "\n".join(lines)
print(f"RAW TEXT: {repr(text)}")  # showing the raw values of the variable
print()
print(text)


pyperclip.copy(text)
