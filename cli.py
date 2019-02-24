import click
import spotipy
from artist import Artist
from spotify_ops import sp

@click.command(help="Find artists who have collaborated with the artist you provide.")
@click.option('--artist_name', prompt="Artist name")
def search(artist_name):
    limit = 10
    search_results = []
    response = sp.search(q=artist_name, type='artist', limit=limit)
    
    for artist in response['artists']['items']:
        pair = (artist['name'], artist['uri'])
        search_results.append(pair)
    
    for i, pair in enumerate(search_results, 1):
        print(str(i) + ". " + pair[0])
    
    selection = click.prompt("Which artist would you like to explore?", default=1, type=int)
    
    if selection < 1 or selection > limit:
        raise click.BadParameter('selection must be between 1 and ' + str(limit))
    
    selected_artist = search_results[selection-1]
    name = selected_artist[0]
    uri = selected_artist[1]
    
    print("Finding collaborators with " + name + "...")
    artist_data = Artist(uri)
    for collab_uri in artist_data.collaborators:
        collab_name = sp.artist(collab_uri)['name']
        print("- " + collab_name)

if __name__ == "__main__":
    search()