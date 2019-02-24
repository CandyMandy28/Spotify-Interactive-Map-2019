import spotipy

class Edge:
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2
        self.songList = set()

    def addSong(self, track):
        self.songList.add(track)

    def getSongList(self):
        return self.songList