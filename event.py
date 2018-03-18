import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Event:
    def __init__(self, prompt, body, rew, rewQty, room):
        #Event's name
        self.name = prompt
        #Event's description
        self.text = body
        #Event's reward type (Item, coins, etc.) String.
        self.reward = rew
        #Event's reward quantity. Integer.
        self.reward_amount = rewQty
        #Room it happens in. Room object.
        self.room = room
        room.addEvent(self)
    def happen(self):
        clear()
        print(self.text)
        print()
        print("You got " + str(self.reward_amount) + " " + self.reward + "!")
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addEvent(self)
    def delete(self):
        for i in range(self.room.events):
            if self.room.events[i].name == self.name:
                self.room.events.pop(i)
