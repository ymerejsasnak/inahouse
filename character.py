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
POSSESSIVE = {'M': 'his', 'F': 'her'}

    
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
        
        # aspects of personality that don't change
        self.outlook = r.choice(['pessimist', 'optimist'])
        self.interpersonal = r.choice(['introvert', 'extrovert'])
        
        # aspects of character that can easily change throughout story
        self.anxiety = r.randint(0, 10)        # 0 serene to 10 panic attack
        self.anger = r.randint(0, 10)          # 0 fine to 10 raging
        
        self.inventory = []
        self.location = 'bedroom'

    def get_primary_feeling(self):
        stats = [self.anxiety, self.anger]
        if max(stats) < 6:
            return 'fine'
        elif self.anger == max(stats):
            return 'angry'
        elif self.anxiety == max(stats):
            return 'anxious'
        
    def move(self):
        # go to new room (based on anxiety level)
        if self.anxiety > r.randint(1, 5):
            # make new list without current room, then pick one
            other_rooms = list(ROOMS)
            other_rooms.remove(self.location)
            self.location = r.choice(other_rooms)
            return self.full_name + ' enters the ' + self.location + '. '
        # or stay in current room
        else:
            return self.full_name + ' stays in the ' + self.location + '. '
        
    def act(self):
        self_feeling = self.get_primary_feeling()
        
        if self_feeling == 'fine':
            if 1 == r.randint(1, 2):
                self.anxiety = self.anxiety + 1
                self.anger = self.anger + 1
                return PRONOUNS[self.sex].capitalize() + ' stares at the wall. '
            else:
                self.anger = self.anxiety + 1
                return PRONOUNS[self.sex].capitalize() + ' hums quietly. '
        elif self_feeling == 'anxious' and self.outlook == 'optimist':
            if 1 == r.randint(1, 2):
                self.anxiety = max(10, self.anxiety + 1)
                return PRONOUNS[self.sex].capitalize() + ' paces the room. '
            else:
                self.anxiety = self.anxiety - 2
                return PRONOUNS[self.sex].capitalize() + ' tries to breathe more slowly. '
        elif self_feeling == 'anxious' and self.outlook == 'pessimist':
            if 1 == r.randint(1, 2):
                self.anxiety = max(10, self.anxiety + 1)
                return PRONOUNS[self.sex].capitalize() + ' gnaws on ' + POSSESSIVE[self.sex] + ' fingernails. '
            else:
                self.anxiety = self.anxiety - 4
                return PRONOUNS[self.sex].capitalize() + ' begins to cry. '            
        elif self_feeling == 'angry':
            if 1 == r.randint(1, 2):
                self.anger = self.anger - 4
                return PRONOUNS[self.sex].capitalize() + ' punches the wall. '
            else:
                self.anger = max(10, self.anger + 1)
                return PRONOUNS[self.sex].capitalize() + ' clenches ' + POSSESSIVE[self.sex] + ' fists. '
    
    def speak(self, other, line=1):
        self_feeling = self.get_primary_feeling()
        other_feeling = other.get_primary_feeling()
        
        # third character in a room is ignored (easier to code, but is interesting too)
        if self == other and self.interpersonal == 'extrovert':
            self.anger = max(10, self.anger + 1)
            return '\n\t"Hello?  Why are you two ignoring me?" asked ' + self.first_name + '. '
        elif self == other and self.interpersonal == 'introvert':
            self.anxiety = max(10, self.anxiety + 1)
            return '''\n\t"Fine, then don't talk to me," ''' + self.first_name + ' whispered. '
        
        else:
            if line == 1:
                if self.interpersonal == 'extrovert':
                    return '\n\t"How are you, ' + other.first_name + '?" asked ' + self.first_name + '. '
                else:
                    self.anxiety = max(10, self.anxiety + 1)
                    return '\n\t"Um, hi," said ' + self.first_name + '. '
            elif line == 2:
                if other.interpersonal == 'introvert' and self.interpersonal == 'introvert':
                    self.anxiety = max(10, self.anxiety + 1)
                    return '\n\t' + self.first_name + ' looked away.'
                elif other.interpersonal == 'introvert':
                    self.anger = max(10, self.anger + 1)
                    return '\n\t"' + other.first_name + ''', don't be so shy," said ''' + self.first_name + '. '
                elif self_feeling == 'fine' or self.interpersonal == 'introvert':
                    self.anxiety = max(10, self.anxiety + 1)
                    return '''\n\t"I'm feeling fine, I guess," said ''' + self.first_name + '. '
                else:
                    self.anxiety = min(0, self.anxiety - 1)
                    self.anger = min(0, self.anger - 1)
                    return '''\n\t"I'm feeling a bit ''' + self_feeling + '," said ' + self.first_name + '. '
            


   
    
    
