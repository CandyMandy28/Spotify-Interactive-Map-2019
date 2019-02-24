import spotipy
import spotify_ops
from spotify_ops import sp

class Artist:
    def __init__(self, id, ):
        self.id = id

        request = sp.artist(id)

        self.name = request['name']
        self.popularity = request['popularity']
        self.images = request['images']
        self.url = request['external_urls']['spotify']
        self.uri = request['uri']
        self.collaborators = set()
        
        self.albums = set()
        self.tracks = set()
        
        self._populate()

    def __repr__(self):
        return self.uri
    
    def __str__(self):
        return self.name
        
    def __hash__(self):
        hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def _populate(self):
        self.albums = spotify_ops.artist_albums_set(self.id)

        for album_id in self.albums:
            track_ids = spotify_ops.album_tracks_set(album_id)
            for track in track_ids:

                artists_set = spotify_ops.track_artists_set(track) 
                if len(artists_set) > 1:
                    for artist_id in artists_set:
                        if artist_id != self.id:
                            self.collaborators.add(artist_id)

# glass_animals = Artist("spotify:artist:4yvcSjfu4PC0CYQyLy4wSq")
# print(glass_animals)
# print(glass_animals.collaborators)