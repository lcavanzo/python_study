#! python3

# map_it.py - This is what your program does:
"""
mapIt.py - Launches a map in the browser using an address from the
    command line or clipboard

tasks:
Gets a street address from the command line arguments or clipboard
Opens the web browser to the Google Maps page for the address
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Read the clipboard contents.
Call the webbrowser.open() function to open the web browser.
"""

import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    addr = "+".join(sys.argv[1:])
    address = addr.replace(",", "")
else:
    addr = pyperclip.paste().replace(" ", "+")
    address = addr.replace(",", "")


def open_browser(link):
    prefix = "https://www.google.com/maps/place/"
    print(f"{prefix}{link}")
    webbrowser.open(f"{prefix}{link}")


open_browser(address)
