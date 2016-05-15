import random as r
import datetime
import setting, character, item


INTERVALS_PER_SCENE = 16 * 4  # 16 hours split into 15 minute segments


class Narrator():
    '''Main controller object that creates other objects (setting, character, item 
    object) and stores them, keeps track of time and locations, and translates all
    into narrative language.  Also give it a style function that adds 'stylistic
    flair' into the narrative (repetitions, fragments, etc etc).
    *note on scenes:  scene1 will be basic intro to story, characters, setting, etc
    with basic movements/interactions.  scene 2 will throw some outside influences
    in to heighten drama/tension/conflict.  scene 3 will move from scene 2 and 
    potentially trigger more extreme behavior from characters.
    (example:  if outlook + interpersonal < 2 and scene == 3 then suicide)'''
    
    def __init__(self):
        self.story = ''
        self.setting = setting.Setting()
        self.characters = [character.Character() for i in range(3)]
        self.time = datetime.datetime(1, 1, 1, 8)  # start at 8am
        
        #items
        
        #act - story progresses from act I to act III, which will hopefully
            #influence character actions (more interesting/intense things as acts go on)
    
    def increment_time(self):
        self.time += datetime.timedelta(minutes=15)
        variation = r.randint(-5, 5) # just for variation to printed time
        self.story += '\n\tAt ' + (self.time + datetime.timedelta(minutes=variation)).strftime('%I:%M %p') + ' '
        
        
    def action(self):
        for character in self.characters:
            self.story += character.move()
            self.story += character.act()
        # and make sure setting object knows where characters are now
        self.setting.update_occupants(self.characters)
        # if characters are in the same room, trigger dialogue:
        for characters in self.setting.occupants.values():
            if len(characters) > 1:
                self.story += characters[0].speak(characters[1], line=1)
                self.story += characters[1].speak(characters[0], line=2)
            if len(characters) > 2:
                self.story += characters[2].speak(characters[2])  #3rd character ignored by other 2 (temporarily?)
    
    

    


# main program for now
n = Narrator()
for i in range(INTERVALS_PER_SCENE):
    n.increment_time()
    n.action()
    
print(n.story)

#also basic temp save
with open('storytemp.txt', 'w') as story_file:
    story_file.write(n.story)
