#!/usr/bin/python

class charClass():
	def __init__(self, t):
		self.title = t

	#ACCESSORS
	def titleReturn(self):
		return(self.title)
		
	#Determine health based on class
	def healthReturn(self):
		if (self.title == "rogue"):
			health = 15
		elif (self.title == "hunter"):
			health = 30
		elif (self.title == "paladin"):
			health = 45
		elif (self.title == "warrior"):
			health = 35
		return(health)