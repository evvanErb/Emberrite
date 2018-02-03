#!/usr/bin/python
import itemClass

#Healing potion
class healthPotion(itemClass.item):
	def __init__(self,name="Health Potion",healAmnt=5):
		itemClass.item.__init__(self,name)
		self.healAmnt = healAmnt
	def heal(self,character):
		character.heal(self.healAmnt)
		return("\n[*] You have been healed " + str(self.healAmnt) + " hit points")

class superHealthPotion(healthPotion):
	def __init__(self):
		healthPotion.__init__(self,"Super Health Potion",15)