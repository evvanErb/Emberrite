#!/usr/bin/python
import random
import people
import characterClasses
import races

#Creating player character
def characterCreation():
	playRaces = ["human","elf","dwarf","half-elf"]
	alignments = ["chaotic good","neutral good","lawful good","chaotic neutral","neutral","lawful neutral","chaotic evil","neutral evil","lawful evil"]
	classes = ["rogue","hunter","paladin","warrior"]

	name = raw_input("\nWhat is your name?\n>>> ")
	gender = raw_input("\nAre you a boy or a girl? (m or f)\n>>> ").lower()
	age = raw_input("\nHow old are you?\n>>> ")

	#Get player race
	charRace = raw_input("\nWhat race are you?\n>>> ").lower()
	while (charRace not in playRaces):
		print("\n[!] Non-playable race! Please enter one of the following:")
		print(playRaces)
		charRace = raw_input("\nWhat race are you?\n>>> ").lower()
	charRace = races.race(charRace)
		
	#Get player class type
	classType = raw_input("\nWhat class are you?\n>>> ").lower()
	while (classType not in classes):
		print("\n[!] Non-playable class! Please enter one of the following:")
		print(classes)
		classType = raw_input("\nWhat class are you?\n>>> ").lower()
	
	#Get player alignment
	if (classType == "paladin"):
		alignment = "lawful good"
	else:
		alignment = raw_input("\nWhat alignment are you?\n>>> ").lower()
		while (alignment not in alignments):
			print("\n[!] Non-playable alignment! Please enter one of the following:")
			print(alignments)
			alignment = raw_input("\nWhat alignment are you?\n>>> ").lower()
	#Create charClass object
	classType = characterClasses.charClass(classType)
	#Get characters health based on class
	health = classType.healthReturn()

	#Randomly generate stats
	stats = {"strength":0,"dexterity":0,"charisma":0,"intelligence":0,"wisdom":0,"constitution":0}
	for stat in stats:
		stats[stat] = random.randint(10,18)
	#Return player
	return(people.character(name,gender,age,charRace,classType,alignment,stats,health,health))