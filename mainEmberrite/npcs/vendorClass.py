#!/usr/bin/python
import npcClass

#vendors
class vendor(npcClass.npc):
	def __init__(self,name,health,armor,damageDeal,inventory):
		npcClass.npc.__init__(self,name,health,armor,damageDeal)
		self.inventory = inventory
		
	def returnInventory(self,character):
		return(self.inventory)