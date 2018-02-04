#!/usr/bin/python
from items import item

class armor(item):
	def __init__(self,name,armorClass,bodyPart):
		item.__init__(self,name)
		self.armorClass = armorClass
		self.bodyPart = bodyPart
	
	def returnArmorClass(self):
		return(self.armorClass)
		
	def returnBodyPart(self):
		return(self.bodyPart)