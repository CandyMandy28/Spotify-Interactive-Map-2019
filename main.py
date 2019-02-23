import spotipy
import config
import node
import branch

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=config.client_id, client_secret=config.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None


artist = sp.artist("64KEffDW9EtZ1y2vBYgq8T")



print("test")
#print(artist)
thisArtist = node.Node(artist)
thisBranch = branch.Edge("first", "second")


#spotify:artist:64KEffDW9EtZ1y2vBYgq8T