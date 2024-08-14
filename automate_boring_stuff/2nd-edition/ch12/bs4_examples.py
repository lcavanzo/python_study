import bs4

example_file = open("./example.html")
example_soup = bs4.BeautifulSoup(example_file.read(), "html.parser")
elems = example_soup.select("#author")

print(type(elems))  # elems is a list of Tag objects
