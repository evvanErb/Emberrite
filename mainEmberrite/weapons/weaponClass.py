#!/usr/bin/python
from items import item

class weapon(item):
	def __init__(self,name,damage,weapRange,bonus,hands):
		item.__init__(self,name)
		self.damage = damage
		self.weapRange = weapRange
		self.bonus = bonus
		self.hands = hands
	
	def returnDamage(self):
		return(self.damage)
		
	def returnWeapRange(self):
		return(self.weapRange)
		
	def returnBonus(self):
		return(self.bonus)
	
	def returnHands(self):
		return(self.hands)
		
	def returnTotalDamage(self):
		return(self.damage + self.bonus)