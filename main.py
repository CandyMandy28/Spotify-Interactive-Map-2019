import spotipy
import config
import network
from artist import Artist

import spotify_ops

import plotly 
plotly.tools.set_credentials_file(username=config.plotly_user, api_key=config.plotly_api_key)

sp = spotify_ops.sp

artist = Artist("64KEffDW9EtZ1y2vBYgq8T")



print("test")
#print(artist)
thisNetwork = network.Network()
thisArtist = network.Node(artist.id, thisNetwork)
thisBranch = network.Edge("first", "second", thisNetwork)


#spotify:artist:64KEffDW9EtZ1y2vBYgq8T
# playlists = sp.user_playlists('spotify')
# print(playlists)
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None


# import plotly.plotly as py
# import plotly.graph_objs as go

# import networkx as nx

# G=nx.random_geometric_graph(50,0.125)
# pos=nx.get_node_attributes(G,'pos')

# dmin=1
# ncenter=0
# for n in pos:
#     x,y=pos[n]
#     d=(x-0.5)**2+(y-0.5)**2
#     if d<dmin:
#         ncenter=n
#         dmin=d

# p=nx.single_source_shortest_path_length(G,ncenter)



# edge_trace = go.Scatter(
#     x=[],
#     y=[],
#     line=dict(width=0.5,color='#888'),
#     hoverinfo='none',
#     mode='lines')

# for edge in G.edges():
#     x0, y0 = G.node[edge[0]]['pos']
#     x1, y1 = G.node[edge[1]]['pos']
#     edge_trace['x'] += tuple([x0, x1, None])
#     edge_trace['y'] += tuple([y0, y1, None])

# node_trace = go.Scatter(
#     x=[],
#     y=[],
#     text=[],
#     mode='markers',
#     hoverinfo='text',
#     marker=dict(
#         showscale=True,
#         # colorscale options
#         #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#         #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#         #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#         colorscale='YlGnBu',
#         reversescale=True,
#         color=[],
#         size=10,
#         colorbar=dict(
#             thickness=15,
#             title='Node Connections',
#             xanchor='left',
#             titleside='right'
#         ),
#         line=dict(width=2)))

# for node in G.nodes():
#     x, y = G.node[node]['pos']
#     node_trace['x'] += tuple([x])
#     node_trace['y'] += tuple([y])


# for node, adjacencies in enumerate(G.adjacency()):
#     node_trace['marker']['color']+=tuple([len(adjacencies[1])])
#     node_info = '# of connections: '+str(len(adjacencies[1]))
#     node_trace['text']+=tuple([node_info])

# fig = go.Figure(data=[edge_trace, node_trace],
#              layout=go.Layout(
#                 title='<br>Network graph made with Python',
#                 titlefont=dict(size=16),
#                 showlegend=False,
#                 hovermode='closest',
#                 margin=dict(b=20,l=5,r=5,t=40),
#                 annotations=[ dict(
#                     text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
#                     showarrow=False,
#                     xref="paper", yref="paper",
#                     x=0.005, y=-0.002 ) ],
#                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

# py.iplot(fig, filename='networkx')