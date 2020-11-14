def make_album(artist_name, album_title, song_numbers=None):
    """printing information about an album"""
    album = {}
    album[artist_name] = album_title
    if song_numbers:
        album['songs_number'] = int(song_numbers)
    return album

active = True
albums = {}
while active:
    artist_name = input("What is the artist's name? ")
    album_title = input("What is the album's title? ")
    answer = input("Do you know the number of song? ")
    if answer == 'yes':
        song_numbers = input("How many songs the album have? ")
    else:
        song_numbers = None
    albums = make_album(artist_name, album_title,song_numbers)
    print(albums)
    flag = input("save another record? ")
    if flag == 'no':
        break

