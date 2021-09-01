import random
import re

class Responder:

    def __init__(self, name, dictionary):
        self.name = name
        self.dictionary = dictionary

    def response(self, input):
        return ''

    def get_name(self):
        return self.name

class RepeatResponder(Responder):
    def response(self, input):
        return '{}ってなに？'.format(input)

class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)

    self.responses = []

    rfile = open('dics/random.tct', 'r', encoding = 'utf_8') 

    r_lines = rfile.readlines()
    rfile.close()

    for line in r_lines:
        str = line.restrip('¥n')
        if (str!=''):
            self.responses.append(str)



    def response(self, input):
        return random.choice(self.dictionary.random)
        

class PatternResponder(Responder):
    def response(self, input):

        for ptn, prs in zip(
            self.dictionary.pattern['pattern'],
            self.dictionary.pattern['phrases']
        ):
            m = re.search(ptn, input)
        if m:
            self.resp = ptn_item.choice(mood)
        if self.resp != None:
            return re.sub('%match%', m.group(), self.resp)

        return random.choice(self.dictionary.random) 
