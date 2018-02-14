#!/usr/bin/python
import functions
import roomLocator
import battles

class room:
	def __init__(self, location, adjacents, description, dark, inventory, containers, monsters, bed, people):
		#room location number
		self.location = location
		#array of adjacents room numbers, -1 if no room there
		self.adjacents = adjacents
		#description of room
		self.description = description
		#boolean for if torch needed
		self.dark = dark
		#items that can be taken in room
		self.inventory = inventory
		#containers holding items
		self.containers = containers
		#monsters in room
		self.monsters = monsters
		#bed in room
		self.bed = bed
		#people in room that can interact with player
		self.people = people
	
	#accessors
	def returnLocation(self):
		return(self.location)
	
	def manager(self, hero, inv):
		while(True):
    		#check if monster in room
			if(len(self.monsters) > 0):
    			#if monster health greater than 0
				if(self.monsters[0].returnHealth() > 0):
    				#print monster name
					print("\nYou've encountered a " + str(self.monsters[0].returnName()) + "!")
					#start battle
					battles.battle(hero,inv,self.monsters[0]).battleManager()

			#description
			#if dark and torch not lit
			if(self.dark and (not inv.torchStatus())):
				print("\nYou are in a dark room.")
			#else print description
			else:
				print(self.description)
				#if room has inventory
				for i in self.inventory:
					print("\nThere is a " + i.returnName() + " in the room.")
				#if container in room
				for i in self.containers:
					#if container open
					if(self.containers[i][0]):
						#iterate over container contents
						for c in range(1, len(self.containers[i])):
							print("\nThere is a " + self.containers[i][c].returnName() + " in the room.")

			#Player choice
			choice = raw_input("\n>>> ").lower()
			
			#rooms
			if ((choice == "n") or (choice == "north")):
				if(self.adjacents[0] >= 0):
					return(roomLocator.getRoom(self.adjacents[0], hero, inv))
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "s") or (choice == "south")):
				if(self.adjacents[1] >= 0):
					return(roomLocator.getRoom(self.adjacents[1], hero, inv))
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "e") or (choice == "east")):
				if(self.adjacents[2] >= 0):
					return(roomLocator.getRoom(self.adjacents[2], hero, inv))
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "w") or (choice == "west")):
				if(self.adjacents[3] >= 0):
					return(roomLocator.getRoom(self.adjacents[3], hero, inv))
				else:
					print("\n[!] You can not go that way!")
					continue
				
			#look around
			elif (choice == "look"):
				continue

			#if there is a bed then the player can sleep
			elif ((choice == "sleep") and (self.bed)):
				hero.heal(5)
				print("\n[*] You slept and now have " + str(hero.returnHealth()) + " hitpoints.")
				continue

			#Check for standard option
			else:
				print(functions.standardOptions(choice, hero, inv, self.inventory, self.containers, self.people, self.location))
				continue