"""As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them."""

class MusicTracker():

    def __init__(self):
        self.listened_to = []
    
    def add(self,track):
        if track == '':
            raise Exception("Please provide a track.")
        self.listened_to.append(track)
