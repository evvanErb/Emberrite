#!/usr/bin/python
import random
import functions
import npcs
import battles
import people
import items
import weapons
import armors

class castleRooms:
    def __init__(self,inv,hero):
    	self.inv = inv
		self.hero = hero
		self.gates()
    
    def gates(self):
        #Description
		print("\nYou are in a giant iron archway. There are giant oak doors to the East belonging to an even grander castle before you.\nThere is a stone path leading West.")
		#Player choice
		choice = raw_input("\n>>> ").lower()
		if ((choice == "w") or (choice == "west")):
			return(self.graveyard())
		elif ((choice == "e") or (choice == "east")):
			return(self.antiChamber())
		elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south")):
			print("\n[!] You can not go that way!")
			return(self.gates())
		elif (choice == "look"):
			return(self.gates())

		#Check for standard option
		else:
			print(functions.standardOptions(choice,self.hero,self.inv))
			return(self.gates())