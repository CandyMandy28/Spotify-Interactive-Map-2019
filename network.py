import spotipy
import spotify_ops
from spotify_ops import sp


class Node:
    def __init__(self, artist_id, network):
        self.id = artist_id
        self.network = network

        self.artist = sp.artist(artist_id)
        self.radius = self.artist['popularity']
        self.pics = self.artist['images']
        self.url = self.artist['external_urls']['spotify']
        self.collaborators = set()


    def find_collab(self):
        album_ids = spotify_ops.artist_albums_set(self.id)
        for album_id in album_ids:
            track_ids = spotify_ops.album_tracks_set(album_id)
            for track_id in track_ids:
                artist_ids = spotify_ops.track_artists_set(track_id)
                for artist_id in artist_ids:
                    if artist_id != self.id:     # doesn't allow the node artist to be in collaborator set
                        self.collaborators.add(artist_id)

    def branch(self):
        for collab in self.collaborators:
            if collab not in self.network.node_ids:
                self.network.node_ids.add(collab)


class Edge:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2
        self.songList = set()

    def addSong(self, track):
        self.songList.add(track)

    def getSongList(self):
        return self.songList

class Network:
    def __init__(self):
        self.node_ids = set()
        self.collab_edges = set()