#!/usr/bin/python
import random
from emberriteClasses.characterClass import character
from emberriteClasses.monsterClass import monster
from emberriteClasses.battleClass import battle
from emberriteClasses.inventoryClass import inventory
from emberriteClasses.potionClass import potions

#Creating player inventory
def inventoryCreation(hero):
	if (hero.returnClassType() == "rogue"):
		return(inventory(hero,["off"],"leather",25,"knife"))

	elif (hero.returnClassType() == "hunter"):
		return(inventory(hero,["off"],"chain-mail",20,"bow"))

	elif (hero.returnClassType() == "paladin"):
		return(inventory(hero,["off"],"plate-mail",10,"hammer"))

	elif (hero.returnClassType() == "warrior"):
		return(inventory(hero,["off"],"chain-mail",20,"short sword"))