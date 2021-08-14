from responder import *
from dictioinary import *


class Ptna:
    def __init__(self, name):
        self.name = name
        self.dictionary = Dictionary()
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
        return self.responder.response(input)

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name
        
            
