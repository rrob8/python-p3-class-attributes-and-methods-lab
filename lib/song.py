class Song:


    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count ={}

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
        
    @classmethod
    def add_to_genres(cls, genre):
        
        if genre in Song.genres:
            pass
        else:
            Song.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist in Song.artists:
            pass
        else:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    @classmethod 
    def add_to_artist_count(cls, artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1