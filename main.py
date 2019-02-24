import spotipy
import config
import spotify_ops
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotify_ops.sp

playlists = sp.user_playlists('spotify')
print(playlists)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None