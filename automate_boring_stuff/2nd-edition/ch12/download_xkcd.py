#! python3

# # download_xkcd.py - Downloads every single XKCD comic.

"""
Here’s what your program does:

Loads the XKCD home page
Saves the comic image on that page
Follows the Previous Comic link
Repeats until it reaches the first comic
This means your code will need to do the following:

Download pages with the requests module.
Find the URL of the comic image for a page using Beautiful Soup.
Download and save the comic image to the hard drive with iter_content().
Find the URL of the Previous Comic link, and repeat.
"""
import os

import bs4
import requests

url = "https://xkcd.com/"  # Starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd

while not url.endswith("#"):
    # Download the page
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of teh comic image
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        # Download the image
        print(f"Downloading image {comic_url}")
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd
    image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Get the prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prev_link.get("href")

print("Done")
