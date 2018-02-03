#!/usr/bin/python
import vendorClass

class barmaid(vendorClass.vendor):
	def __init__(self,name,health,armor,damageDeal,inventory):
		vendorClass.vendor.__init__(self,name,health,armor,damageDeal,inventory)
		
	def conversation(self, hero, inv):
		convo = True
		while (convo):
			purchase = raw_input("\n'ello love what can I get for you?\n>>> ")
			if (purchase == "room"):
				if (inv.returnGold() >= 20):
					print("\nThat'll be 20 gold pieces. Thanks!")
					hero.heal(20)
					inv.spendGold(20)
				else:
					print("\nSorry love you don't have enough gold!")
			elif (purchase == "drink" or purchase == "mead" or purchase == "beer" or purchase == "ale" or purchase == "meat"):
				if (inv.returnGold() >= 5):
					print("\nThat'll be 5 gold pieces. Thanks!")
					inv.spendGold(5)
				else:
					print("\nSorry love you don't have enough gold!")
			elif ((purchase == "stop") or (purchase == "leave") or (purchase == "bye") or (purchase == "goodbye")):
				convo = False
			else:
				print("\nSorry love we don't have that!")