#!/usr/bin/python
import os

#Welcome text
def title():
	#Print icon
	here = os.path.dirname(os.path.abspath(__file__))
	infile = open(here+"/Icon.txt", "r")
	icon = infile.read()
	infile.close
	print(icon)
	#Print welcome
	print("\nWelcome to Emberrite!!!")
	print("Created by Evvan Erb. Powered by Python.")