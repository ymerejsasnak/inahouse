import random as r


ROOMS = ['bathroom', 'kitchen', 'living room', 'bedroom', 'basement'] 

FIRST_NAMES = {
    'M': ['Alex', 'Burt', 'Calvin', 'Diego', 'Eric', 'Frank', 'George', 
    'Harold', 'Ivan', 'Kevin', 'Lawrence', 'Manuel', 'Oliver', 'Percy', 'Salvatore'],
    'F': ['Brenda', 'Christine', 'Evelyn', 'Gretta', 'Iris', 'Juanita', 
    'Katie', 'Lucinda', 'Mary', 'Noor', 'Olive', 'Patricia', 'Tatyana', 'Ursula']
        }
LAST_NAMES = ['Alvarez', 'Burton', 'Dutton', 'Fortunado', 'Ives', 'Jenkins',
    'Kolchek', 'Liszewski', 'Ng', 'Placensio', 'Quint', 'Undermann', 'Zyk']
    
PRONOUNS = {'M': 'he', 'F': 'she'}
    
    
class Character():
    '''These are the main actors of the story (of course!).  All aspects randomized
    at instantiation.  Most 'traits' will be a value between 0 and 10.  Also some
    true/false personality flags (some of which may be rarer than others).  Also stores
    inventory if they pick up objects, method of speaking for dialogue and 
    catch-phrases if any.  Name, physical description, mood, memories (old and story-based), 
    typical behaviors, etc.  Shoudl there also be a protagonist flag to follow
    one main character, or should the narrative just jump around and follow them all?'''
        
    #future ideas:
    #memories, preferred rooms, preferred objects, hated rooms/objects
    #typical behaviors/actions (maybe just lists of words to say sometimes?)
    
    def __init__(self):
        # basics
        self.sex = r.choice(['M', 'F'])
        self.first_name = r.choice(FIRST_NAMES[self.sex])
        self.last_name = r.choice(LAST_NAMES)
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = r.randint(20, 50)
        
        # status flags
        self.alive = True
        self.awake = True        
        
        # aspects of personality that don't change (or change little/slowly)
        self.outlook = r.randint(0, 10)         # 0 totally pessimistic to 10 totally optimistic
        self.interpersonal = r.randint(0, 10)   # 0 totally introverted to 10 totally extroverted
        self.attractiveness = r.randint(0, 10)  # 0 ugly to 10 gorgeous
        
        # aspects of character that can easily change throughout story
        self.hunger = r.randint(0, 10)         # 0 totally sated to 10 starving
        self.sleepiness = r.randint(0, 10)     # 0 totally rested to 10 exhausted
        self.pain_pleasure = r.randint(0, 10)  # 0 excruciating to 10 orgasmic
        self.happiness = r.randint(0, 10)      # 0 suicidal to 10 euphoric
        self.anxiety = r.randint(0, 10)        # 0 serene to 10 panic attack
        self.anger = r.randint(0, 10)          # 0 fine to 10 raging
        
        self.inventory = []
        self.location = 'bedroom'

    def move(self):
        # go to new room
        if 1 < r.randint(1, 2):
            # make new list without current room, then pick one
            other_rooms = list(ROOMS)
            other_rooms.remove(self.location)
            self.location = r.choice(other_rooms)
            return self.full_name + ' enters the ' + self.location + '. '
        # or stay in current room
        else:
            return self.full_name + ' stays in the ' + self.location + '. '
        
    def act(self):
        return PRONOUNS[self.sex].capitalize() + ' looks around. ' # dummy action for now
    
    def speak(self, other):
        if self == other:
            return '\n\t"What about me?" said ' + self.first_name
        else:
            if self.interpersonal + self.happiness > 6:
                return '\n\t"Hello, ' + other.first_name + '," said ' + self.first_name + '. '
            else:
                return '\n\t"I just want to be alone," said ' + self.first_name + '. '
                
        
        
   
    
    
