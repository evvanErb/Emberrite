#!/usr/bin/python
import random
import items
import weapons
import armors

#Dealing with standard options
def standardOptions(choice,hero,inv, roomInv, roomContainers, roomPeople, roomLocation):
	#Check inventory
	if (choice == "inventory"):
		strToRet = ""
		for i in inv.returnInv():
			if(type(i) is str):
				strToRet += (i + ", ")
			else:
				strToRet += i.returnName() + ", "
		return(strToRet)
	
	#Clear screen
	elif (choice == "clear"):
		return("\n"*50)

	#Manage torch
	elif (choice == "check torch"):
		if (inv.torchStatus()):
			return("\n[*] Torch is on")
		else:
			return("\n[*] Torch is off")
	elif (choice == "change torch"):
		return(inv.changeTorch())
	elif (choice == "light torch"):
		if (not inv.torchStatus()):
			return(inv.changeTorch())
		else:
			return("\n[!] Torch is already on")
	
	#Manage weapon
	elif ((choice == "change weapon") or (choice == "equip weapon")):
		weaponChoice = raw_input("\nEnter the weapon you would like to equip\n>>> ")
		#iterate over inventory to check for weapons
		for i in range(len(inv.returnInv())):
			#if item is of type weapon
			if (isinstance(inv.returnInv()[i], weapons.weapon)):
				#if weapon has same name as chosen weapon equip
				if(inv.returnInv()[i].returnName() == weaponChoice):
					#Check if weapon compatible with class while equipping it
					temp = inv.returnWeapon()
					if(inv.equipWeapon(weaponChoice)):
						inv.addItem(temp)
						inv.removeItem(inv.returnInv()[i])
						return("\n[*] Weapon changed to " + weaponChoice)
					else:
						return("\n[!] That weapon is not compatible with your class!")
		#else return not in inv
		return("\n[!] That weapon is not in your inventory")
		
	elif (choice == "check weapon"):
		return(inv.returnWeapon())

	#Manage armor
	elif ((choice == "change armor") or (choice == "equip armor")):
		armorChoice = raw_input("\nEnter the armor you would like to equip\n>>> ")
		#iterate over inventory to check for weapons
		for i in range(len(inv.returnInv())):
			#if item is of type weapon
			if (isinstance(inv.returnInv()[i], armors.armor)):
				#if weapon has same name as chosen weapon equip
				if(inv.returnInv()[i].returnName() == armorChoice):
					#Check if weapon compatible with class while equipping it
					temp = inv.returnArmor()
					if(inv.equipArmor(armorChoice)):
						inv.addItem(temp)
						inv.removeItem(inv.returnInv()[i])
						return("\n[*] Armor changed to " + armorChoice)
					else:
						return("\n[!] That armor is not compatible with your class!")
		#else return not in inv
		return("\n[!] That weapon is not in your inventory")
		
	elif (choice == "check armor"):
		return(inv.returnArmor())
	
	#Manage gold
	elif (choice == "check gold"):
		return(inv.returnGold())

	#Manage health
	elif (choice == "check health"):
		return(hero.returnHealth())
	
	#Potions
	elif (choice == "drink health potion"):
		#iterate over inventory to check for health potion
		for i in range(len(inv.returnInv())):
			#if item is of type health potion
			if (isinstance(inv.returnInv()[i], items.healthPotion)):
				#make sure its a regular health potion and not super one
				if(inv.returnInv()[i].returnName().lower() == "health potion"):
					#heal hero and delete item from inventory
					inv.returnInv()[i].heal(hero)
					inv.removeItem(inv.returnInv()[i])
					return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
		#else return its not in inv
		return("\n[!] That is not in your inventory!")

	elif (choice == "drink super health potion"):
		#iterate over inventory to check for health potion
		for i in range(len(inv.returnInv())):
			#if item is of type health potion
			if (isinstance(inv.returnInv()[i], items.superHealthPotion)):
				#heal hero and delete item from inventory
				inv.returnInv()[i].heal(hero)
				inv.removeItem(inv.returnInv()[i])
				return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
		#else return its not in inv
		return("\n[!] That is not in your inventory!")
		
	#Examine command not a command
	elif (choice[:7] == "examine"):
		return("\n[!] There is nothing out of the ordinary.")
	
	#If there is nothing to search for
	elif (choice == "search"):
		return("\n[!] You found nothing!")
	
	#The letter from the mailbox
	elif (choice == "read letter"):
		for i in range(len(inv.returnInv())):
			if("letter" == inv.returnInv()[i].returnName()):
				return("\nWelcome to Emberrite!")
			else:
				return("\n[!] That can not be read!")
	
	#The cake
	elif ((choice == "take cake") and (roomLocation == 5)):
		return("\n[!] The cake is a lie!")
	
	#Exit game
	elif (choice =="exit"):
		exit()
	
	#List commands with menu options
	elif((choice == "menu") or (choice == "help")):
		return("\nDirections:\nNorth\nSouth\nEast\nWest\n\nCommands:\ninventory - lists your inventory\nsearch - searches room\nlight torch - lights torch\nchange torch - changes torch\ncheck torch - checks torch's current status\ncheck health - prints current health\ncheck armor - checks armor equipped\ncheck weapon - checks equiped weapon\ncheck gold - checks how much gold you have\nequip weapon - equip new weapon\nequip armor - equip new armor")

	#Items that can not be taken/opened/closed
	#if user trys to take an item
	if (choice[:4] == "take"):
		for i in range(len(roomInv)):
			#if in invetnory
			if (choice[5:] == roomInv[i].returnName()):
				toAdd = roomInv[i]
				inv.addItem(toAdd)
				roomInv.pop(i)
				return("\n[*] " + toAdd.returnName() + " taken.")
		#check containers
		for i in roomContainers:
			#if container open
			if(roomContainers[i][0]):
				#iterate over container contents
				for c in range(1, len(roomContainers[i])):
					#if item in container
					if(choice[5:] == roomContainers[i][c].returnName()):
						addedItem = roomContainers[i][c]
						inv.addItem(addedItem)
						roomContainers[i].pop(c)
						return("\n[*] " + addedItem.returnName() + " taken.")
		#if  item not in room or in closed container
		return("\n[!] That item can not be taken!")
	#get version of take
	if (choice[:3] == "get"):
    		for i in range(len(roomInv)):
			#if in invetnory
			if (choice[4:] == roomInv[i].returnName()):
				toAdd = roomInv[i]
				inv.addItem(toAdd)
				roomInv.pop(i)
				return("\n[*] " + toAdd.returnName() + " taken.")
		#check containers
		for i in roomContainers:
			#if container open
			if(roomContainers[i][0]):
				#iterate over container contents
				for c in range(1, len(roomContainers[i])):
					#if item in container
					if(choice[4:] == roomContainers[i][c].returnName()):
						addedItem = roomContainers[i][c]
						inv.addItem(addedItem)
						roomContainers[i].pop(c)
						return("\n[*] " + addedItem.returnName() + " taken.")
		#if  item not in room or in closed container
		return("\n[!] That item can not be taken!")
						
	#if user trys to open a container
	elif (choice[:4] == "open"):
		if (choice[5:] in roomContainers):
			roomContainers[choice[5:]][0] = True
			return("\n[*] " + choice[5:] + " opened.")
		#If it can not be opened
		else:
			return("\n[!] That can not be opened!")

	#if user trys to close a container
	elif (choice[:5] == "close"):
		if (choice[6:] in roomContainers):
			roomContainers[choice[6:]][0] = False
			return("\n[*] " + choice[6:] + " closed.")
		#If it can not be closed
		else:
			return("\n[!] That can not be closed!")

	#talk to people in room
	elif (choice[:7] == "talk to"):
		for i in range(len(roomPeople)):
			if(choice[8:] == roomPeople[i].returnName()):
				roomPeople[i].conversation(inv)
				return("")
		#if person not in roomPeople
		return("\n[!] You can not talk to them!")

	#Unknown commands
	else:
		return("\n[!] Unknown command...")