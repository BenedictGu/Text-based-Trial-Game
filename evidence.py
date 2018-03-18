import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Evidence:
    def __init__(self, name, desc, room):
        self.name = name
        self.desc = desc
        self.loc = None
        self.room = room
        room.addEvidence(self)
    def describe(self):
        clear()
        print(self.name + ":")
        print()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addEvidence(self)

    def showDescription(self):
        print(self.name + ":")
        print()
        print(self.desc)
        print()
        input("press enter to continue...")

    def noticeCollected(self):
        clear()
        print(self.name + ":")
        print()
        print(self.desc)
        print()
        print(self.name + " collected!")
        input("press enter to continue...")
