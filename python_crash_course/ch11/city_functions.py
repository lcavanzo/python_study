
def city_country(city, country, population=''):
    """Generate a nearly formatted city-country information"""
    if population:
        full_country = f"{city}, {country} - population {population}"
    else:
        full_country = f"{city}, {country}"
    return full_country.title()

