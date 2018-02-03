#!/usr/bin/python

#Welcome text
def title():
	#Print icon
	infile = open("Icon.txt", "r")
	icon = infile.read()
	infile.close
	print(icon)
	#Print welcome
	print("\nWelcome to Emberrite!!!")
	print("Created by Evvan Erb. Powered by Python.")