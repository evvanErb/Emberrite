#!/usr/bin/python
import random
from people import *

#Creating player inventory
def inventoryCreation(hero):
	if (hero.returnClassName() == "rogue"):
		return(inventory(hero,["off"],"leather",25,"knife"))

	elif (hero.returnClassName() == "hunter"):
		return(inventory(hero,["off"],"chain-mail",20,"bow"))

	elif (hero.returnClassName() == "paladin"):
		return(inventory(hero,["off"],"plate-mail",10,"hammer"))

	elif (hero.returnClassName() == "warrior"):
		return(inventory(hero,["off"],"chain-mail",20,"short sword"))