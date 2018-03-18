import random


class Character:
    def __init__(self, name, room, quote):
        self.name = name
        self.room = room
        self.quote = quote
        room.addCharacter(self)
    def moveTo(self, room):
        self.room.removeCharacter(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeCharacter(self)
    def dialogue(self, line):
        print(line)
        print()
        input("Press enter to continue...")
