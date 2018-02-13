#!/usr/bin/python
import maps

#iterate over all rooms and return appropriate room based on cordinates
def getRoom(location, hero, inv):
	#iterate over central rooms
	for i in range(len(maps.centralRooms)):
		#if room in central
		if(location == maps.centralRooms[i].returnLocation()):
			return(maps.centralRooms[i].manager(hero, inv))
	"""		
	#iterate over castle rooms
		for i in range(len(maps.castleRooms)):
			#if room in central
			if(location == maps.castleRooms[i].returnLocation()):
				return(maps.castleRooms[i].manager(hero, inv))
	"""
				
	#if room not found
	return("You cant go that way!")