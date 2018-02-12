#!/usr/bin/python
import maps

#iterate over all rooms and return appropriate room based on cordinates
def getRoom(location, hero, inv):
	#iterate over central rooms
	for i in range(len(centralRooms)):
		#if room in central
		if(location == centralRooms[i].returnLocation()):
			return(centralRooms[i].manager(hero, inv))
			
	#iterate over castle rooms
		for i in range(len(castleRooms)):
			#if room in central
			if(location == castleRooms[i].returnLocation()):
				return(castleRooms[i].manager(hero, inv))
				
	#if room not found
	return("You cant go that way!")