import spotipy
import config
from spotipy.oauth2 import SpotifyClientCredentials

_client_credentials_manager = SpotifyClientCredentials(client_id=config.client_id, client_secret=config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=_client_credentials_manager)

glass_animals_id = "spotify:artist:4yvcSjfu4PC0CYQyLy4wSq"

def get_artist_tracks(artist_id):
    albums = sp.artist_albums(artist_id)
    print(albums)

get_artist_tracks(glass_animals_id)