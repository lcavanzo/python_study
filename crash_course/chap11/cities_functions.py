
def get_formatted_city(city, country, population=''):
    if population:
        city_info = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_info = f"{city.title()}, {country.title()}"
    return city_info



