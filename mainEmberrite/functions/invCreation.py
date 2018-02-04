#!/usr/bin/python
import weapons
import people

#Creating player inventory
def inventoryCreation(hero):
	if (hero.returnClassName() == "rogue"):
		return(people.inventory(hero,["off"],"leather",25,weapons.weapon("knife",4,5,0,1)))

	elif (hero.returnClassName() == "hunter"):
		return(people.inventory(hero,["off"],"chain-mail",20,weapons.weapon("bow",4,50,0,2)))

	elif (hero.returnClassName() == "paladin"):
		return(people.inventory(hero,["off"],"plate-mail",10,weapons.weapon("hammer",6,5,0,1)))

	elif (hero.returnClassName() == "warrior"):
		return(people.inventory(hero,["off"],"chain-mail",20,weapons.weapon("short sword",6,5,0,1)))