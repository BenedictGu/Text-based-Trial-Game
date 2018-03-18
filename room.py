import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.desc = description
        self.characters = []
        self.exits = []
        self.evidences = []
        self.events = []
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addEvidence(self, evid):
        self.evidences.append(evid)
    def removeEvidence(self, evid):
        self.evidences.remove(evid)
    def addCharacter(self, character):
        self.characters.append(character)
    def removeCharacter(self, character):
        self.characters.remove(character)
    def addEvent(self, event):
        self.events.append(event)
    def removeEvent(self, event):
        self.events.remove(event)
    def hasEvidence(self):
        return self.evidences != []
    def getEvidenceByName(self, name):
        for i in self.evidences:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasCharacter(self):
        return self.characters != []
    def getCharacterByName(self, name):
        for i in self.characters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
