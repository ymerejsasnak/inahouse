import random as r


# lists/dicts from which to choose options for character creation
FIRST_NAMES = {
    'M': ['Alex', 'Burt', 'Calvin', 'Diego', 'Eric', 'Frank', 'George', 
    'Harold', 'Ivan', 'Kevin', 'Lawrence', 'Manuel', 'Oliver', 'Percy', 'Salvatore'],
    'F': ['Brenda', 'Christine', 'Evelyn', 'Gretta', 'Iris', 'Juanita', 
    'Katie', 'Lucinda', 'Mary', 'Noor', 'Olive', 'Patricia', 'Tatyana', 'Ursula']
        }
LAST_NAMES = ['Alvarez', 'Burton', 'Dutton', 'Fortunado', 'Ives', 'Jenkins',
    'Kolchek', 'Liszewksi', 'Ng', 'Placensio', 'Quint', 'Undermann', 'Zyk']
    
    
class Character():
    '''These are the main actors of the story (of course!).  All aspects randomized
    at instantiation.  Most 'traits' will be a value between 0 and 1.  Also some
    true/false personality flags (some of which may be rarer than others).  Also stores
    inventory if they pick up objects, method of speaking for dialogue and 
    catch-phrases if any.  Name, physical description, mood, memories (old and story-based), 
    typical behaviors, etc.  Shoudl there also be a protagonist flag to follow
    one main character, or should the narrative just jump around and follow them all?'''
    
    def __init__(self):
        # basics
        self.sex = r.choice(['M', 'F'])
        self.first_name = r.choice(FIRST_NAMES[self.sex])
        self.last_name = r.choice(LAST_NAMES)
        self.age = r.randint(20, 50)
        
        # aspects of personality that don't change (or change little/slowly)
        self.outlook = r.uniform(0, 1)         # 0 totally pessimistic to 1 totally optimistic
        self.interpersonal = r.uniform(0, 1)   # 0 totally introverted to 1 totally extroverted
        self.attractiveness = r.uniform(0, 1)  # 0 ugly to 1 gorgeous
        
        # aspects of character that can easily change throughout story
        self.hunger = r.uniform(0, 1)         # 0 totally sated to 1 starving
        self.sleepiness = r.uniform(0, 1)     # 0 totally rested to 1 exhausted
        self.pain_pleasure = r.uniform(0, 1)  # 0 excruciating to 1 orgasmic
        self.happiness = r.uniform(0, 1)      # 0 suicidal to 1 euphoric
        self.anxiety = r.uniform(0, 1)        # 0 serene to 1 panic attack
        self.anger = r.uniform(0, 1)          # 0 fine to 1 raging
        
        
        #memories, preferred rooms, preferred objects, hated rooms/objects
        #typical behaviors/actions (maybe just lists of words to say sometimes?)
        

# define an 'act' method that determines what the char will do on each 'turn'
#(this will be called by narrator for each char)

    
# !!!!  note:  can use .__dict__ to show/access all attributes/values given an object
        
        
    
    
