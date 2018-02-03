#!/usr/bin/python2
import functions
import maps

functions.title()
hero = functions.characterCreation()
inv = functions.inventoryCreation(hero)
print("\n[*] Character created!")
maps.rooms(inv,hero)