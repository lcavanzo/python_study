# idiot.py -  How to Keep an Idiot Busy for Hours

"""
Let’s use PyInputPlus to create a simple program that does the following:

1. - Ask the user if they’d like to know how to keep an idiot busy for hours.
2. - If the user answers no, quit.
3. - If the user answers yes, go to Step 1.

"""

import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep an idiot busy for hours?\n"
    response = pyip.inputYesNo(prompt)

    if response.lower() == "no":
        print("Thank you. Have a nice day :)")
        break
