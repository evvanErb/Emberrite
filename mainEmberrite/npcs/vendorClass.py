#!/usr/bin/python
import npcClass
import items

#vendors
class vendor(npcClass.npc):
	def __init__(self,name,health,armor,damageDeal,inventory):
		npcClass.npc.__init__(self,name,health,armor,damageDeal)
		self.inventory = inventory
		
	#accessors
	def returnInventory(self,character):
		return(self.inventory)
	
	#mutators
	def sellItem(self,toBuy,playerInv):
		#Check if item in vendor inv
		for i in self.inventory:
			#if custom class
			if(isinstance(i, items.item)):
				if(toBuy == i.returnName()):
					#Check if player has enough gold to buy
					if(playerInv.returnGold() >= self.inventory[i]):
						price = self.inventory[i]
						#sell item to player
						playerInv.spendGold(price)
						playerInv.addItem(i)
						self.inventory.pop(i)
						return("\nThat'll be " + str(price) + " gold pieces. Thanks!")
					#if not enough gold
					else:
						return("\nYou don't have enough gold for that!")
			#if not custom class
			else:
				if(toBuy == i):
					#Check if player has enough gold to buy
					if(playerInv.returnGold() >= self.inventory[i]):
						price = self.inventory[i]
						#sell item to player
						playerInv.spendGold(price)
						playerInv.addItem(i)
						self.inventory.pop(i)
						return("\nThat'll be " + str(price) + " gold pieces. Thanks!")
					#if not enough gold
					else:
						return("\nYou don't have enough gold for that!")
		#if vendor doesnt have it
		return("\nI don't have that!")
	
	#convo
	def conversation(self,playerInv):
		service = True
		while (service):
			#list inventory
			for i in self.inventory:
				#if custom class
				if(isinstance(i, items.item)):
					print("\nI have a " + i.returnName() + " in-stock.")
				else:
					print("\nI have a " + i + " in-stock.")
			#Ask player for input
			purchase = raw_input("\nWhat can I get for you?\n>>> ")
			#If player wants to buy something
			if (purchase[:3] == "buy"):
				buyingItem = raw_input("\nWhat would you like to buy?\n>>> ")
				print(self.sellItem(buyingItem,playerInv))
			#Stop convo
			elif ((purchase == "stop") or (purchase == "leave")):
				service = False
			else:
				print("\nI can't do that!")