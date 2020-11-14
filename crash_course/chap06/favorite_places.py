favorite_places = {}

for names in range(3):
    places = []
    name = input("What's your name? ")
    for number_of_places in range(3):
        place = input(f"favorite place {number_of_places + 1} ")
        places.append(place)
    favorite_places[name] = places

for name, values in favorite_places.items():
    print(f"\n{name.title()} you favorites places are: ")
    for place in values:
        print(f"\t{place.title()}")
