# -*- coding: utf-8 -*-
import spotipy
import config
from spotipy.oauth2 import SpotifyClientCredentials

_client_credentials_manager = SpotifyClientCredentials(client_id=config.client_id, client_secret=config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=_client_credentials_manager)

glass_animals_id = "spotify:artist:4yvcSjfu4PC0CYQyLy4wSq"
celeste_album_id = "spotify:album:5OZHQ7KG8k04IOkF50fACO"

"""
Return a set of album IDs belonging to an artist.
"""
def artist_albums_set(artist_id):
    paging_offset = 0
    paging_limit = 50
    albums = set()
    
    while True:
        response = sp.artist_albums(artist_id, limit=paging_limit, offset=paging_offset)
        albums = set()
        
        paging_offset += paging_limit
        
        for album in response['items']:
            albums.add(album['id'])
            print(album['id'], album['name'])

        if not response['next']:
            break
    
    return albums

"""
Return a set of track IDs belonging to an album.
"""
def album_tracks_set(album_id):
    paging_offset = 0
    paging_limit = 50 
    tracks = set()

    while True:
        response = sp.album_tracks(album_id, offset=paging_offset, limit=paging_limit)

        paging_offset += paging_limit
        
        for track in response['items']:
            tracks.add(track['id'])
            # print(track['id'], track['name'])

        if not response['next']:
            break
    
    return tracks