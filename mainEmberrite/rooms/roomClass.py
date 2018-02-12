#!/usr/bin/python
import maps

class room:
	def __init__(self, location, adjacents, description, dark, inventory, containers):
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
	
	def manager(self, hero, inv):
		while(True):
			#description
			#if dark and torch not lit
			if(dark and (not self.inv.torchStatus())):
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
					if(i[0]):
						#iterate over container contents
						for c in range(1, len(i)):
							print("\nThere is a " + i[c].returnName() + " in the room.")

			#Player choice
			choice = raw_input("\n>>> ").lower()
			
			#rooms
			if ((choice == "n") or (choice == "north")):
				if(self.adjacents[0] > 0):
					return(getRoom(self.adjacents[0]), hero, inv)
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "s") or (choice == "south")):
				if(self.adjacents[1] > 0):
					return(getRoom(self.adjacents[1]), hero, inv)
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "e") or (choice == "east")):
				if(self.adjacents[2] > 0):
					return(getRoom(self.adjacents[2]), hero, inv)
				else:
					print("\n[!] You can not go that way!")
					continue
				
			elif((choice == "w") or (choice == "west")):
				if(self.adjacents[3] > 0):
					return(getRoom(self.adjacents[3]), hero, inv)
				else:
					print("\n[!] You can not go that way!")
					continue
				
			#look around
			elif (choice == "look"):
				continue
			
			#if input greater than 5
			elif(len(choice) > 5):
				#if user trys to take an item
				if (choice[:5] == "take "):
					for i in range(len(self.inventory)):
						#if in invetnory
						if (choice[6:] == self.inventory[i].returnName()):
							toAdd = self.inventory[i]
							inv.addItem(toAdd)
							self.inventory.pop(i)
							print("\n[*] " + toAdd.returnName() + " taken.")
							continue
					#check containers
					else:
						for i in self.containers:
							#if container open
							if(i[0]):
								#iterate over container contents
								for c in range(1, len(i)):
									addedItem = i[c]
									inv.addItem(addedItem)
									i.pop(c)
									print("\n[*] " + addedItem.returnName() + " taken.")
									continue
									
				
				#if user trys to open a container
				if (choice[:5] == "open "):
					if (choice[6:]in self.containers):
						self.containers[choice[7:]][0] = True
						print("\n[*] " + choice[6:] + " opened.")
						continue
			
			#if user trys to open a container
			elif(len(choice) > 6):
				if (choice[:6] == "close "):
					if (choice[7:] in self.containers):
						self.containers[choice[7:]][0] = False
						print("\n[*] " + choice[7:] + " closed.")
						continue

			#Check for standard option
			else:
				print(functions.standardOptions(choice, hero, inv))
				continue