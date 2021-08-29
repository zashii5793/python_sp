import random
import re
from tkinter.constants import SEPARATOR

class Dictionary:
    def __init__(self):
        self.random = []
        rfile = open('random.txt', 'r', encoding = 'utf-8')
        r_lines = rfile.readlines()
        rfile.close()

        for line in r_lines:
            str = line.rstrip('¥n')

            if (str!= ''):
                self.random.append(str)

        pfile = open('pattern.txt', 'r', encoding='utf-8')
        p_lines = pfile.readlines()
        pfile.close()
        
        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('¥n')
            if (str!=''):
                self.new_lines.append(str)

        self.pattern = []
        for line in self.new_lines:
            ptn, prs = line.split('¥t')
            self.pattern.setdefault('pattern', []).append(ptn)
            self.pattern.setdefault('pattern', []).append(prs)

class ParseItem:
    SEPARATOR = '^((-?¥d+)##)?(.*)$'

    def __init__(self, pattern, phrases):
        m = re.findall(ParseItem.SEPARATOR, pattern)
        self.modify = 0

        if m[0][1]:
            self.modify = int(m[0][1]) 
        self.pattern = m[0][2] 
        self.phrases = []
        self.dic = {}

        for phrase in phrases.split('|'):
            m = re.findall(ParseItem.SEPARATOR, phrase)
            self.dic['need'] = 0
            if m[0][1]:
                self.dic['need'] = int(m[0][1])
            self.dic['phrases'] = m[0][2]
            self.phrases.append(self.dic.copy())
    def match(self, str):
        return re.search(self.pattern, str)

    def choice(self, mood):
        choices = []
        for p in self.phrases:
            if (self.suitable(p['need'], mood)):
                choices.append(p['phrase'])
        if (len(choices) == 0):
            return None        
        return random.choice(choices) 

    def suitable(self, need, mood):
        if (need == 0):
            return True
        elif (need > 0):
            return (mood > need)
        else:
            return (mood < need) 
