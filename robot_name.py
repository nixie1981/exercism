import random
import string
class Robot(object):
    def __init__(self):
        characters = []
        for i in range(2):
            characters.append(random.choice(string.ascii_uppercase))
        for i in range(3):
            characters.append(random.choice(string.digits))
        self.name = ''.join(characters)
    def reset(self):
        characters = []
        for i in range(2):
            characters.append(random.choice(string.ascii_uppercase))
        for i in range(3):
            characters.append(random.choice(string.digits))
        self.name = ''.join(characters)
        
        