import random as r


# rooms that are always used
GIVEN_ROOMS = ['bathroom', 'kitchen', 'living room', 
    'first bedroom', 'second bedroom', 'third bedroom']
# rooms that are sometimes added
EXTRA_ROOMS = ['basement', 'spare bedroom', 'dining room', 'empty room', 'attic']


class Setting():
    '''Creates and stores the rooms that make up the house which is the setting.
    Picks from a list of possible rooms, with possible adjectives (that link to
    certain flags that trigger certain aspects of characters), all of which
    can possibly influence the characters.  Also will keep track of room contents
    (both characters and item objects).  Also put possible random events here
    that exist beyond the characters (ie, run out of food, fire in the house, etc)'''
    
    def __init__(self):
        self.rooms = []
        self.rooms.extend(GIVEN_ROOMS)
        extras = r.randint(0, 5)
        self.rooms.extend(r.sample(EXTRA_ROOMS, extras))
            
        
