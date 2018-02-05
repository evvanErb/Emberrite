#!/usr/bin/python
import random
import functions
import npcs
import battles
import people
import items
import weapons
import armors

class castleRooms:
    def __init__(self,inv,hero):
    	self.inv = inv
		self.hero = hero
		self.gates()
    
    def gates(self):
        return("GATES")