#!/usr/bin/python2
import functions
import maps
import rooms

functions.title()
hero = functions.characterCreation()
inv = functions.inventoryCreation(hero)
print("\n[*] Character created!")
rooms.getRoom(0).manager(hero, inv)