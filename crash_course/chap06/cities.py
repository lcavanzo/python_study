####### EXAMPLE ######
#    'veracruz': {
#        'country' : 'mexico',
#        'population' : '100',
#        'fact' : 'great city'
#        },
#    'cdmx': {
#        'country' : 'mexico',
#        'population' : '1000',
#        'fact' : 'bad city'
#        }
#}
#
#print(cities)
#######
cities = {}

for _ in range(3):
    city = input("Put a city name: ")
    country = input("What it is country?  ")
    population= input("the population is: ")
    fact= input("a funny fact is?: ")
    cities[city] = {}
    cities[city]['country'] = country
    cities[city]['population'] = population
    cities[city]['fact'] = fact

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in city_info.items():
        print(f"\t{key}: {value}")



