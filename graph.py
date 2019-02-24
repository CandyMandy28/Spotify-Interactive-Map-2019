from pynteractive import *
import network
import artist

graph = Graph(directed = False)
a.view()

# adding nodes
a.addNode()
a.addNode(10)
a.addNode(11,color='red')
a.addNode('john',shape='star',color='green')

# adding edges
a.addEdge(1,10)
a.addEdge(1,'john',style='dash-line')
a.addEdge(1,11,width='4')
a.addEdge(10,11,width='2',label='hello world')

# def startGraph(artist):
#     graph.view()
#     firstArtist(artist)

# def firstArtist(artist):
#     graph.addNode(artist.name, radius=20)

# def addArtist(artist):
#     graph.addNode(artist.name, radius=10)

# # add edge to the nodes
# def addConnection(artist, other_artist, album):
#     pass

# def clear():
#     graph.clear()