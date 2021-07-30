from responder import *

class ptna:
    def __init__(self, name):
        self.name = name
        self.responder = RandomResponder('Random')

    def dialogue(self, input):
        return self.responder.response(input)

    def get_responder        