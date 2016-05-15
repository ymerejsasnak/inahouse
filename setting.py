import random as r


ROOMS = ['bathroom', 'kitchen', 'living room', 'bedroom', 'basement'] 


class Setting():
    '''Creates and stores the rooms that make up the house which is the setting.
    Keeping simple for now with a given list of rooms.  Maybe later add random
    rooms and more importantly add possible descriptors for the rooms that can
    trigger certain character actions and/or affect character stats.  For now
    load them into a dict that keeps track of 'contents' and 'occupants'.'''
    
    def __init__(self):
        self.contents = {key: [] for key in ROOMS}
        self.occupants = {key: [] for key in ROOMS}
            
    def update_occupants(self, characters):
        # clear old locations
        self.occupants = {key: [] for key in ROOMS}
        # then update with new ones
        for character in characters:
            self.occupants[character.location] = character
        
