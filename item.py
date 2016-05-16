import random as r


POSSIBLE_ITEMS = {
    'bathroom':
        {'placement': ['on the counter', 'on the floor', 'in the sink'],
         'item': ['sliver of soap', 'half-full shampoo bottle', 'damp towel']},
    'kitchen':
        {'placement': ['on the counter', 'in the fridge', 'on the table'],
         'item': ['dirty plate', 'piece of rotten meat', 'cracked glass']},
    'living room':
        {'placement': ['on the mantle', 'on the coffee table', 'on the floor'],
         'item': ["faded picture of someone's family", 'cracked porcelain angel']},
    'bedroom':
        {'placement': ['on the bed', 'in the closet', 'on the nightstand'],
         'item': ['locked diary', 'single sock', 'hand mirror']},
    'basement':
        {'placement': ['on a workbench', 'on the floor', 'behind the furnace'],
         'item': ['rusty hammer', 'bottle of bleach', 'moldy blanket']}
    }

class Item():
    '''Items to be found throughout the house that the characters can interact
    with.  Will store the room it's found in, and [this one probably just as
    text?] its location within that room (ie, on table, on the floor, etc).  Each
    will be an adjective noun combination.  Certain nouns and adj will have 
    associated values that add/subtract from certain character stats'''
    #actually item traits should maybe be 0 to 1 also (ie, ugliness/beauty, $ value,
    #nothing/meaningful, size, etc
    
    def __init__(self, location):
        self.item = r.choice(POSSIBLE_ITEMS[location]['item'])
        self.placement = r.choice(POSSIBLE_ITEMS[location]['placement'])
        
        #and stats
