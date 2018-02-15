#!/usr/bin/python

import rooms
import items
import people
import npcs
import weapons
import armors

castleRooms=[
	#(location, adjacent rooms[n,s,e,w], description, dark, inventory, containers, monsters, bed, people, secret passageways[n,s,e,w])
	rooms.room(34, [-1,-1,-1,-1], "\nDescription", False, [], {}, [], False, [], [False, False, False, False]),

]