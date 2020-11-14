


pets = [
        {
            'name' : 'calvin',
            'kind' : 'dog',
            'age'  : '3'
        },
        {
            'name' : 'marie',
            'kind' : 'cat',
            'age' :  '2'
        },
        {
            'name' : 'alv',
            'kind' : 'fish',
            'age'  : '5'
        }
]

for animal in pets:
    print(f"{animal['name']} is a {animal['kind']} and has " 
        f"{animal['age']} years" )
