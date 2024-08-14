#! python3

# searchpypi.py  - Opens several search results.

"""
write a script to do this with the search results page for
the Python Package Index at https://pypi.org/.

This is what your program does:

Gets search keywords from the command line arguments
Retrieves the search results page
Opens a browser tab for each result
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Fetch the search result page with the requests module.
Find the links to each search result.
Call the webbrowser.open() function to open the web browser.
"""

import sys
import webbrowser

import bs4
import requests

print("Searching ...")  # display text while downloading the search result page
res = requests.get(
    "https://google.com/search?q="
    "https://pypi.org/search/?q=" + " ".join(sys.argv[1:])
)
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
link_elems = soup.select(".package-snippet")
num_open = min(5, (len(link_elems)))

if len(link_elems) == 0:
    print("No links found")
else:
    for i in range(num_open):
        url_to_open = "https://pypi.org" + link_elems[i].get("href")
        print(f"Opening {url_to_open}")
        webbrowser.open(url_to_open)
