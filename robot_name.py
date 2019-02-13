import random
import string
class Robot(object):
    robot_names = []
    @classmethod
    def give_name(cls):
        characters = []
        for i in range(2):
            characters.append(random.choice(string.ascii_uppercase))
        for i in range(3):
            characters.append(random.choice(string.digits))
        name = ''.join(characters)
        if name in cls.robot_names:
            name = cls.give_name()
        else:
            cls.robot_names.append(name)
        return name
    def __init__(self):
        self.name = Robot.give_name()
    def reset(self):
        self.name = Robot.give_name()
        
        