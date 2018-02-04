#!/usr/bin/python
import random
import items
import weapons
import armors

#Dealing with standard options
def standardOptions(choice,hero,inv):
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
	elif (choice == "change weapon"):
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
	elif (choice == "change armor"):
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
	
	#Items that can not be taken/opened/closed
	elif (choice[:4] == "take"):
		return("\n[!] That can not be taken!")
	elif (choice[:4] == "open"):
		return("\n[!] That can not be opened!")
	elif (choice[:5] == "close"):
		return("\n[!] That can not be closed!")
		
	#Examine command not a command
	elif (choice[:7] == "examine"):
		return("\n[!] There is nothing out of the ordinary.")
	
	#If there is nothing to search for
	elif (choice == "search"):
		return("\n[!] You found nothing!")
	
	#The letter from the mailbox
	elif ((choice == "read letter") and ("letter" in inv.returnInv())):
		return("\nWelcome to Emberrite!")
	
	#Exit game
	elif (choice =="exit"):
		exit()
	
	#Unknown commands
	else:
		return("\n[!] Unknown command...")