import spotipy
import spotify_ops
from spotify_ops import sp
from artist import Artist


class Node:
    def __init__(self, artist_id, network):
        self.id = artist_id
        self.network = network
        self.artist = Artist(artist_id)

    def branch(self):
        for collab in self.artist.collaborators:
            if collab in self.network.node_ids:
                pass
            else:
                self.network.addNode(collab)
                self.network.addEdge(self.id, collab)

class Edge:
    def __init__(self, id1, id2, network):
        self.ids = {id1, id2}
        self.songList = set()
        self.network = network

    def addSong(self, track):
        self.songList.add(track)

    def getSongList(self):
        return self.songList

class Network:
    def __init__(self):
        self.node_ids = set()
        self.nodes = set()
        self.collab_edges = set()

    def addNode(self, nodeID):
        self.nodes.add( Node(nodeID, self) )
        self.node_ids.add(nodeID)

    def addEdge(self, id1, id2):
        self.collab_edges.add( Edge(id1, id2, self))