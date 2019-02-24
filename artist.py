import spotipy
import spotify_ops
from spotify_ops import sp

class Artist:
    def __init__(self, id):
        self.id = id

        request = sp.artist(id)

        self.name = request['name']
        self.popularity = request['popularity']
        self.images = request['images']
        self.url = request['url']
        self.collaborators = set()

    def