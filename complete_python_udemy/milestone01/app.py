""" 
milestone01
movies library
add, search, delete a movie by its year, tittle, director 
"""

movies = [
        {
            'title': "Rush",
            'year': "2013", 
            'director': "Ron Howard"
        },
        {
            'title': "Lord Of The Ring", 
            'year': "2005", 
            'director': "Peter Jackson"
        },
        {
            'title': "Avatar",
            'year': "2009",
            'director': "James Cameron"
        },
]

def add_movie(movie):
    title = input("movie title >>> ")
    year = input("release year >>> ")
    director = input("movies's director >>> ")
    new_movie = {'title': title, 'year': year, 'director': director}
    movie.append(new_movie)


def find_movie(movie):
    search = input("Movie to find >>> ")
    if search.lower() == movie[0]['title'].lower():
        print("\n>>> The movie is in our library <<<")
    else:
        print("\n>>> Sorry, that movie would be included soon <<<")



def delete_movie(movies):
    to_delete = input("What movie do you want to delete? >>> ")
    count = 0
    for movie in movies:
        print(movie)
        if to_delete.lower() == movie['title'].lower():
            print(f"{to_delete.title()} deleted ...")
            movie.pop(count)
        count =+ 1

    

def list_movies(movies):
    for movie in movies:
        print(f"""
        title: {movie['title']};
        year: {movie['year']};
        director: {movie['director']}
        """, sep=' ')


def menu():
    MENU_PROMPT = """
    'a' to add a movie,
    'f' to find a movie,
    'd' to delete a movie,
    'l' to lists all the movies,
    'q' to quit: 
    >>> """

    options =        {
            'f': find_movie,
            'a': add_movie,
            'd': delete_movie,
            'l': list_movies,
            'q': "q"
        }

    running = True
    while running:
        answer = input(MENU_PROMPT)
        option = options[answer]
        if answer == 'f':
            option(movies)
        elif answer == 'a':
            option(movies)
        elif answer == 'd':
            option(movies)
        elif answer == 'l':
            option(movies)
        else:
            print("Bye ...")
            running = False



def main():
    menu()

main()
