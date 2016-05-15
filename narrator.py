import random as r
import setting, character, item

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
        #setting (list of rooms?)
        #list of characters
        #list of objects
        #time (time of day) increment by 15 minutes each 'turn' but if used in story
            #write it as random time + or - 5 minutes of internal time for variation
        #act - story progresses from act I to act III, which will hopefully
            #influence character actions (more interesting/intense things as acts go on)
        pass 
    
