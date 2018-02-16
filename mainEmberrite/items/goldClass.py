import itemClass

#Healing potion
class gold(itemClass.item):
	def __init__(self,name="gold",amount=1):
		itemClass.item.__init__(self,name)
		self.amount = amount
		
	def returnAmount(self):
		return(self.amount)