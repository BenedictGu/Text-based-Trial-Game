from tkinter import *
import math
import random
import time

str_map = """Garbage Room#####   #####    ######
            #   #   #        #    #
            #   # H	#        #    # pharmacologists' lab
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

class Game(Frame):
	def __init__(self, name, console_lines=11):
		self.name = name

		#the agents in the game
		self.rooms = []

		self.characters = []

		self.player = None

		#initialize the graphical user interface
		self.root = Tk()
		self.root.title(name)

		#console1 for map
		self.map_cords = {"garbage_room":[2,14],
						  "workshop":[6,14],
						  "hallway":[10,18],
						  "entrance_hall":[18,18],
						  "lab":[2,32],
						  "classroom":}
		self.map_list = draw_map()
		self.map_list[18][18] = "@"
		self.map = map_list
		self.console1 = Text(self.root, height=15, bg="#000000", fg="#A0F090", width=65)
		self.report_map()
		self.console1.pack()

		#console2 for interaction
		self.console2 = Text(self.root,height=console_lines,bg="#000000",fg="#A0F090",width=65)
		self.console2.pack()

		self.buttons = []
		b1 = Button(self.root, text="Quit", command=self.root.destroy)
		self.buttons.append(b1)
		b1.pack()

	def report_map(self):
		for r in self.map_list:
			s = ""
			for c in r:
				s += c
			self.report("console1", s)

	def report(self, console, line=""):
		line += "\n"
		if console = "console1":
			self.console1.insert(END, line)
			self.console1.see(END)
		elif console = "console2":
			self.console2.insert(END, line)
			self.console2.see(END)
		else:
			print(line)

	def update(self):
		Frame.update(self)
		map_list = draw_map()
		map_list[self.map_cords[self.player.location.name][0]][self.map_cords[self.player.location.name][1]] = "@"
		self.map_list = map_list
		self.report_map()

	def set_player(self, player):
		self.player = player

	def add_window(self, room):
		self.rooms.append(room)

	def add_character(self, character):
		self.characters.append(character)

	def clear(self):
		self.console2.delete(1.0, END)


def draw_map():
		# create the map
		i = 0 # index
		j = 0 # row
		list_map = [[]]
		while i < len(str_map):
			if str_map[i] != "\n":
				list_map[j].append(str_map[i])
			else:
				list_map.append([])
				j += 1
			i += 1
		return list_map




"""
Garbage Room#####   #####    ######
            #   #   #        #    #
            #   # H	#        #    # pharmacologists' lab
            #   # A	#        #    #
            ##### L	##########    #######
workshop    #   # L	                    #
            #   # W                     #
            #   # A	                    #
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
