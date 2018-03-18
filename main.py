from room import Room
from player import *
from evidence import Evidence
from character import Character
from event import Event
from trial import *
import time
import os

"""
(Autopsy Report, Glass Bottle, Sooty Towel) [2, 0]
(Trash Duty, Glass Bottle, Broken Neck) [3, 1]
(Sculptor’s Account, Two Shelves, Fused Glass) [1, 0]
(Autopsy Report, Poison Powder, Journal) [3, 2]
[[2, 0],[3, 1],[1, 0],[3, 2]]
"""
if_skip = input('Do you want to read your previous progress?y/n ')
if if_skip == 'y':
    f = open('save.txt')
    l = f.read()
    if l != '':
        SKIP = True
    else:
        SKIP = False
else:
    SKIP = False

inter = open('intermission.txt')
INTERMISSION = inter.read()

EVIDENCE_NUM = 13
IN_INVEST = False
TIME_LEFT = 2
STR_MAP = """
Garbage Room#####   #####    ######
            #   #   #        #    #
            #   # H	#        #    # pharmacologist's lab
            #   # A	#        #    #
            ##### L	##########    #######
workshop    #   # L #	                #
            #   # W #                   # Classroom
            #   # A	#                   #
            ##### Y	#####################
            #   #   #
            #   #   #
            #####   #
                #   #
                #   #
                #   #
            #####   #####
            #           #
            #           #
            #           #
            ############# Entrance Hall
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#create the window
player = Player()

lab = Room("Pharmacologist's lab", "")
garbage = Room("Garbage Room", "")
workshop = Room("Workshop", "")
entrance = Room("Entrance Hall", "")
hallway = Room("Hallway", "")
classroom = Room("Classroom", "")

Room.connectRooms(lab, "Classroom", classroom, "Pharmacologist's Lab")
Room.connectRooms(garbage, "Hallway", hallway, "Garbage Room")
Room.connectRooms(entrance, "Hallway", hallway, "Entrance Hall")
Room.connectRooms(workshop, "Hallway", hallway, "Workshop")
Room.connectRooms(classroom, "Hallway", hallway, "Classroom")

player.location = entrance

sculptor = Character("The Ultimate Sculptor", classroom, "I believe in us! We can make it out of this twisted place alive!")
diplomat = Character("The Ultimate Diplomat", classroom, "We needn't worry. Rationality will set us free. You of all people understand that, I'm sure.")
fencer = Character("The Ultimate Fencer", classroom, "No time for games. We need to break out before someone cracks.")
hunter = Character("The Ultimate Hunter", lab, "Yo, want to come hang out with me? No point in worrying about all this. I trust you guys.")
priestess = Character("The Ultimate Priestess", lab, "I must have faith that we can escape from this prison. How Job-like!")

autopsy = Evidence("Autopsy Report", "The victim was the Ultimate Pharmacologist. The fatal wound was a blow to the back of the head, which killed him instantly. His time of death was approximately 11 PM last night. No traces of poison were found in his system, though the powder spilled all over him was a lethal dose.", classroom)
poison_powder = Evidence("Poison Powder", "Indeed, some form of powder is spilled all over him, covering his upper chest region and some parts of his arms. The floor under him is also covered in the same powder. There is one small region where it looks like something hit the powder, but it’s no larger than a quarter, and there is no poison on anything else in the room.", classroom)
glass_bottle = Evidence("Glass Bottle", "The glass bottle was found underneath the victim at the time he was discovered, which means that the bottle was on the floor before him. In addition, the bottle was still corked, meaning that before he fell and broke it, it was not harmful. This also means the spread of powder across his chest must have happened after he died.", classroom)
broken_neck = Evidence("Broken Neck", "His head wound appears to have been caused by a fairly small object, actually, considering the size of the wound, but in addition his neck looks broken. Could this be a separate wound? Why would the killer break his neck after his death?", classroom)
sculptor_account = Evidence("sculptor's account", "Talking with the Ultimate Sculptor reveals that she was walking by the classroom several times last night, in order to bring tools from the workshop to her room so she could sculpt without fear of being ambushed. She remembers seeing the Ultimate Pharmacologist in the hallway, who looked at her intensely for just a moment before seeming to recognize who she was and drawing back. However, he was headed away from the classroom and towards the other students’ quarters.", classroom)
vomit = Evidence("Fencer Vomited", "It’s also notable that the Fencer vomited near the body. She claims it was stress. . .", classroom)
full_shelves = Evidence("The Full Shleves", "The Pharmacologist’s room is dominated by two shelves, covering the entirety of the left and right walls. One is completely filled with remedies of every type. There’s herbal mixes, emetic poisons, and prescription drugs all across the wall.", lab)
antidote = Evidence("The Antidote", "The other shelf, however, is almost completely empty, with only one bottle on it. That bottle is labeled \"Bonebane - Antidote\".", lab)
journal = Evidence("The Journal", "In addition, he kept a journal, which is resting on his desk in the back of the room. Flipping through it, the last page appears to be about yesterday’s revelation. It reads:\"It’s time I get rid of everything. I don’t want to be what I am.\"\n\"I can’t keep myself hidden like this. I’m so afraid, but maybe if I tell them individually they won’t turn on me.\"", lab)
fuse = Evidence("Fused Glass", "Once in the trash room, the headmaster appears, evidently frustrated. He goes on a short rant about people not knowing how incinerators work, and when questioned he pulls out a large ball of fused glass. He says it was found melted in the incinerator and was clogging up space, so he removed it.", garbage)
soot = Evidence("Soot", "The inside of the incenerator is covered in soot, meaning that something that produces a lot of smoke was burned recently.", garbage)
sooty_towel = Evidence("Sooty Towel", "There is a towel laying by the side of the furnace, which appears to have been singed by the intense heat. It is also covered in this same kind of soot. Why did the towel not get burned, but was covered in the same soot?", garbage)
duty = Evidence("Trash Duty", "The Hunter brings up that it was the Pharmacologist on trash duty yesterday.", garbage)

chair = Event("Chair", "You lifted the chair and a few coins fell out! Who knows where they were to start.", "coins", 10, workshop)
desk = Event("Desk", "Rummaging around in this desk revealed coins!", "coins", 10, classroom)
penny = Event("Lucky Penny", "You found a lucky penny on the ground! You hope you won't need the luck.", "coins", 1, hallway)

shop = Shop(player)

p = open('prologue.txt')
prelogue_text = p.read()
p.close()


def prelogue():
    clear()
    print_(prelogue_text)

def interm():
    clear()
    print_(INTERMISSION)

def print_status():
    clear()
    s = "You are in " + player.location.name + ".\n"
    s += player.location.desc + "\n"
    s += "The room has the following characters:\n"
    i = 1
    for c in player.location.characters:
        s += str(i) + ". "
        s += c.name + "\n"
        i += 1
    if IN_INVEST:
        s += "\nThe room has the following evidences:\n"
    else:
        s += "\nThe following items look interesting:\n"
    i = 1
    if IN_INVEST:
        for e in player.location.evidences:
            s += str(i) + ". "
            s += e.name + "\n"
            i += 1
    else:
        for e in player.location.events:
            s += str(i) + ". "
            s += e.name + "\n"
            i += 1
    s += "\nYou can go to other rooms:\n"
    z = 1
    for exit in player.location.exits:
        s += str(z) + ". " + exit[0] + "\n"
        z += 1
    print(s)
    print()

def print_my_status():
    clear()
    print("Your current credibility is " + str(player.credibility) + "%.")
    print("You are missing " + str(EVIDENCE_NUM - len(player.evidences)) + " pieces of evidence.\n")

def showMap():
    clear()
    print(STR_MAP)

def showHelp():
    clear()
    print()
    print("input inventory to show the evidences you have collected.")
    print("input map to check out your surroundings!")
    print("input go + <the room's number> to go to another room.")
    print("input invest + <number of item on interesting / evidence list> to investigate something.")
    print("input inspect + <number of evidence> to review a piece of evidence in detail! Check your inventory for the number!")
    print("input help to see this screen, but you already knew that.")
    print("input me to check your credibility! You'll want to stay credible.")
    print('input talk and the number of the person to talk with this particular person.')
    print()
    input("press enter to continue...")

def print_(line=""):
    for c in line:
        time.sleep(0.014)
        print(c, end="")
playing = True
to_trial = True

def epilogue():
    f = open('epilogue.txt')
    print_(f.read())
    f.close()

prelogue()
input("press enter to continue...")

while playing and len(player.evidences) < EVIDENCE_NUM and not SKIP:
    print_status()
    commandSuccess = False
    while not commandSuccess:
        command = input("What now? ")
        if command == "":
            print("Not a valid command.")
        else:
            commandSplit = command.split()
            if commandSplit[0].lower() == "go":
                if len(commandSplit) > 1:
                    if commandSplit[1].isnumeric():
                        index = int(commandSplit[1])
                        if index > 0 and index <= len(player.location.exits):
                            player.goDirection(player.location.exits[index-1][0])
                            commandSuccess = True
                        else:
                            print("Invalid room!")
                    else:
                        if player.location.getDestination(commandSplit[1]) != None:
                            player.goDirection(commandSplit[1])
                            commandSuccess = True
                        else:
                            print("Invalid Room!")
                else:
                    print("Not a valid command.")
            elif commandSplit[0].lower() == "invest":
                if IN_INVEST:
                    if len(commandSplit) > 1:
                        number = int(commandSplit[1])
                        if number >= 1 and number <= len(player.location.evidences):
                            evid = player.pickup(player.location.evidences[number-1])
                            evid.noticeCollected()
                            commandSuccess = True
                        else:
                            print("invalid evidence!")
                    else:
                        print("Not a valid command!")
                else:
                    if len(commandSplit) > 1:
                        number = int(commandSplit[1])
                        if number >= 1 and number <= len(player.location.events):
                            ev = player.location.events[number - 1]
                            clear()
                            player.coins += ev.reward_amount
                            ev.happen()
                            commandSuccess = True
            elif commandSplit[0].lower() == "inventory":
                player.showInventory()
                commandSuccess = True
            elif commandSplit[0].lower() == "help":
                showHelp()
                commandSuccess = True
            elif commandSplit[0].lower() == "map":
                showMap()
                input("press enter to continue...")
                commandSuccess = True
            elif commandSplit[0].lower() == "exit":
                exit()
            elif commandSplit[0].lower() == "me":
                print_my_status()
                input("press enter to continue...")
                commandSuccess = True
            elif commandSplit[0].lower() == "talk":
                if len(commandSplit) > 1:
                    number = int(commandSplit[1])
                    if number >= 1 and number <= len(player.location.characters):
                        clear()
                        player.location.characters[number-1].dialogue(player.location.characters[number-1].quote)
                        commandSuccess = True
                        TIME_LEFT -= 1
            elif commandSplit[0].lower() == "wait":
                clear()
                print("You decided to pass the time in your room.")
                TIME_LEFT -= 1
            elif commandSplit[0].lower() == "inspect":
                if len(commandSplit) > 1:
                    number = int(commandSplit[1])
                    if number >= 1 and number <= len(player.evidences):
                        clear()
                        player.evidences[number-1].describe()
                        commandSuccess = True
            elif commandSplit[0].lower() == 'shop':
                shop.shopping()
                commandSuccess = True
            else:
                print("Not a valid command")
            if TIME_LEFT == 0:
                if not IN_INVEST:
                    interm()
                IN_INVEST = True

trial = Trial(player)
trial.evidences = [[autopsy, glass_bottle, sooty_towel], [duty, glass_bottle, broken_neck], [sculptor_account, full_shelves, fuse], [autopsy, poison_powder, journal], [antidote, vomit, broken_neck, soot], [broken_neck, poison_powder, fuse, duty], [fuse, vomit, broken_neck, autopsy], [full_shelves, antidote, soot, sooty_towel], [sooty_towel, broken_neck, antidote, vomit, poison_powder], [poison_powder, broken_neck, vomit, full_shelves, antidote], [duty, antidote, journal, poison_powder, autopsy], [broken_neck, fuse, autopsy, sculptor_account, full_shelves]]
trial.answers = [[3, 1, False],[4, 2, False],[2, 1, True],[4, 3, True],[2, 1, False],[3, 4, False],[2, 1, True],[1, 3, False],[2, 1, False], [2, 1, False],[3, 4, False],[3, 1, False]]
trial.startTrial(not SKIP)

epilogue()
