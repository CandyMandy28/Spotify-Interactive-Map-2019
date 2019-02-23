import spotipy


class Node:
    def __init__(self, artist):
        self.artist = artist

    def size(self):
        radius = self.artist['popularity']
        print(radius)

    def picture(self):
        pics = self.artist['images']
        print(pics[0]['url'])

    def branch(self):
        print()
        
    def artistLink(self):
        urls = self.artist['external_urls']
        spotifyUrl = urls['spotify']
        print(spotifyUrl)

