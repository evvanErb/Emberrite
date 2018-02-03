#!/usr/bin/python
import random
import items

#Dealing with standard options
def standardOptions(choice,hero,inv):
	#Check inventory
	if (choice == "inventory"):
		return(inv.returnInv())
	
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
		if (weaponChoice in inv.returnInv()):
			temp = inv.returnWeapon()
			inv.equipWeapon(weaponChoice)
			inv.addItem(temp)
			inv.removeItem(weaponChoice)
			return("\n[*] Weapon changed to " + weaponChoice)
		else:
			return("\n[!] That weapon is not in your inventory")
	elif (choice == "check weapon"):
		return(inv.returnWeapon())

	#Manage armor
	elif (choice == "change armor"):
		armorChoice = raw_input("\nEnter the armor you would like to equip\n>>> ")
		if (armorChoice in inv.returnInv()):
			temp = inv.returnArmor()
			inv.equipArmor(armorChoice)
			inv.addItem(temp)
			inv.removeItem(armorChoice)
			return("\n[*] Armor changed to " + armorChoice)
		else:
			return("\n[!] That armor is not in your inventory")
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
		if ("health potion" in inv.returnInv()):
			items.potions("health potion").healthPotion(hero)
			inv.removeItem("health potion")
			return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
		else:
			return("\n[!] That is not in your inventory!")

	elif (choice == "drink super health potion"):
		if ("super health potion" in inv.returnInv()):
			items.potions("super health potion").superHealthPotion(hero)
			inv.removeItem("super health potion")
			return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
		else:
			return("\n[!] That is not in your inventory!")
	
	#Items that can not be taken/opened/closed
	elif (choice[:4] == "take"):
		return("\n[!] That can not be taken!")
	elif (choice[:4] == "open"):
		return("\n[!] That can not be opened!")
	elif (choice[:5] == "close"):
		return("\n[!] That can not be closed!")
	
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