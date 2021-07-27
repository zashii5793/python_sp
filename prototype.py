class Ptna:
    def __init__(self, name):
      self.name = name
      self.responder = Responder('What')

    def dialogue(self, input):
        return self.responder.response(input)

    def get_responder_name(self):
        return self.responder.name

    def get_name(self):
        return self.name

class Responder:
    def __init__(self, name):
        self.name = name

    def response(self, input):
        return '{}ってなに？'.format(input)

    def prompt(obj):
        return obj.get_name() + ":" + obj.get_responder_name() + '> '
    
    print('Ptna System prototype : ptna')
    ptna = Ptna('ptna')

while True:
    inputs = input(' > ')
    if not inputs:
      print('OK')
      break
    response = ptna.dialogue(inputs)
    print(prompt(ptna), response)
