from pynteractive import *
import network
import artist

graph = Graph(directed = False)

def startGraph(artist):
    graph.view()
    firstArtist(artist)

def firstArtist(artist):
    graph.addNode(artist.name, radius=20)

def addArtist(artist):
    graph.addNode(artist.name, radius=10)

# add edge to the nodes
def addConnection(artist, other_artist, album):
    graph.addEdge(  artist.name,
                    other_artist.name,
                    width=4,
                    label=album)

def clear():
    graph.clear()