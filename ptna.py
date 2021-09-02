from responder import *
from dictioinary import *


class Ptna:
    def __init__(self, name):
        self.name = name
        self.dictionary = Dictionary()
        self.emotion = Emotion(self.dictionary)
        self.res_random = RandomResponder('Random', self.dictionary)
        self.res_What = RepeatResponder('Repeat?', self.dictionary)
        self.res_pattern = PatternResponder('Pattern', self.dictionary)

    def dialogue(self, input):
        x = random.randint(1, 100)
        if x <= 60:
            self.responder = self.res_pattern
        elif 61 <= x <= 90:
            self.responder = self.res_random
        else:
            self.responder = self.res_What
        return self.responder.response(input, self.emotion.mood)

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name
        
            
class Emotion:
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5

    def __init__(self, dictionary) :
        self.dictionary = dictionary
        self.mood = 0

    def update(self, input):
        for ptn_item in self.dictionary.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break    
            if self.mood < 0:
                self.mood += Emotion.MOOD_RECOVERY
            elif self.mood > 0:
                self.mood = Emotion.MOOD_RECOVERY

    def adjust_mood(self, val):
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN                        
