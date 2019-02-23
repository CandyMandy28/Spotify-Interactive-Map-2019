import spotipy


class Node:
    def __init__(self, artist):
        self.artist = artist
        self.id = artist['id']
        self.radius = self.artist['popularity']
        self.pics = self.artist['images']
        self.url = self.artist['external_urls']['spotify']
        print(self.url)
        #spotifyUrl = urls['spotify']


    def branch(self):
        print()
        

