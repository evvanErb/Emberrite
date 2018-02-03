#!/usr/bin/python
import random
import people

#Creating player inventory
def inventoryCreation(hero):
	if (hero.returnClassName() == "rogue"):
		return(people.inventory(hero,["off"],"leather",25,"knife"))

	elif (hero.returnClassName() == "hunter"):
		return(people.inventory(hero,["off"],"chain-mail",20,"bow"))

	elif (hero.returnClassName() == "paladin"):
		return(people.inventory(hero,["off"],"plate-mail",10,"hammer"))

	elif (hero.returnClassName() == "warrior"):
		return(people.inventory(hero,["off"],"chain-mail",20,"short sword"))